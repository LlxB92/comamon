# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from datetime import datetime, timedelta

from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    blm_documento = fields.Char(string='Enlace a Documento')
    code = fields.Char(string='Lead Number', default="/", required=False, readonly=False)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    blm_payment_acumulado = fields.Float(string='Acumulado')
    blm_product_id = fields.Many2one('product.product', string='Product Control')
    blm_line_id = fields.Many2one('sale.order.line', string='Linea Control')
    blm_odoo8 = fields.Char(string='Id Odoo 8 Linea de Pedido')

class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    blm_control_facturacion = fields.Boolean(string='Control Facturacion', default=False)
    blm_sale_line_ids = fields.Many2many(
        'sale.order.line',
        'sale_order_line_invoice_rel',
        'invoice_line_id', 'order_line_id',
        string='Sales Order Lines', readonly=True, copy=False)
    blm_odoo8 = fields.Char(string='Id Odoo 8 Linea de Factura')

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    blm_odoo8 = fields.Char(string='Id Odoo 8 Factura')

    @api.multi
    def write(self, values):
        res = super(AccountInvoice, self).write(values)
        invoice_line_obj = self.env['account.invoice.line']
        default_deposit_product_id = self.env['ir.config_parameter'].sudo().get_param('sale.default_deposit_product_id')
        
        if res and default_deposit_product_id:
            blm_anticipo = int(default_deposit_product_id)
            invoice_line = self.env['account.invoice.line'].search([('invoice_id', '=', self.id)])
            if invoice_line:
                for line in invoice_line:
                    if line.blm_control_facturacion is False:
                        if line.product_id.service_policy == 'delivered_timesheet':
                            anticipo_pendiente = line.sale_line_ids.price_subtotal - line.sale_line_ids.blm_payment_acumulado
                            if anticipo_pendiente >= line.price_subtotal:
                                anticipo_sumado = line.price_subtotal
                                sale_line = self.env['sale.order.line'].search([('id', '=', line.sale_line_ids.id)])
                                if sale_line:
                                    taxes = sale_line.product_id.taxes_id.filtered(lambda r: not sale_line.order_id.company_id or r.company_id == sale_line.order_id.company_id)
                                    if sale_line.order_id.fiscal_position_id and taxes:
                                        tax_ids = sale_line.order_id.fiscal_position_id.map_tax(taxes, sale_line.product_id, sale_line.order_id.partner_shipping_id).ids
                                    else:
                                        tax_ids = taxes.ids
                                    anticipo_actualizado = sale_line.blm_payment_acumulado + anticipo_sumado
                                    sale_line.write({'blm_payment_acumulado': anticipo_actualizado})
                                    line.write({'blm_control_facturacion': True})
                                    so_line = invoice_line_obj.create({
                                        'name': _('Advance: %s') % (line.name,),
                                        'price_unit': line.price_unit,
                                        'quantity': line.quantity * -1,
                                        'account_id': 2208,
                                        'product_uom': 1,
                                        'product_id': blm_anticipo,
                                        'uom_id': line.product_id.uom_id.id,
                                        'discount': line.discount,
                                        'account_analytic_id': line.account_analytic_id.id,
                                        'blm_control_facturacion': True,
                                        'invoice_line_tax_ids': [(6, 0, tax_ids)],
                                        'invoice_id': line.invoice_id.id,
                                        'blm_sale_line_ids': [(6, 0, [sale_line.id])]
                                    })
                            elif (anticipo_pendiente < line.price_subtotal) and (anticipo_pendiente > 0):
                                anticipo_sumado = anticipo_pendiente
                                sale_line = self.env['sale.order.line'].search([('id', '=', line.sale_line_ids.id)])
                                if sale_line:
                                    taxes = sale_line.product_id.taxes_id.filtered(lambda r: not sale_line.order_id.company_id or r.company_id == sale_line.order_id.company_id)
                                    if sale_line.order_id.fiscal_position_id and taxes:
                                        tax_ids = sale_line.order_id.fiscal_position_id.map_tax(taxes, sale_line.product_id, sale_line.order_id.partner_shipping_id).ids
                                    else:
                                        tax_ids = taxes.ids
                                    line.write({'blm_control_facturacion': True})
                                    so_line = invoice_line_obj.create({
                                        'name': _('Advance: %s') % (line.name,),
                                        'price_unit': line.price_unit,
                                        'quantity': (sale_line.product_uom_qty - sale_line.qty_invoiced) * -1,
                                        'account_id': 2208,
                                        'product_uom': 1,
                                        'product_id': blm_anticipo,
                                        'uom_id': line.product_id.uom_id.id,
                                        'discount': line.discount,
                                        'account_analytic_id': line.account_analytic_id.id,
                                        'blm_control_facturacion': True,
                                        'invoice_line_tax_ids': [(6, 0, tax_ids)],
                                        'invoice_id': line.invoice_id.id,
                                        'blm_sale_line_ids': [(6, 0, [sale_line.id])]
                                    })
                                    anticipo_actualizado = sale_line.blm_payment_acumulado + anticipo_sumado
                                    sale_line.write({'blm_payment_acumulado': anticipo_actualizado})

            self.compute_taxes()
            # self._onchange_cash_rounding()
        # en local
        # 'product_id': 70,
        # en local CUENTA DE ANTICIPO
        # 'account_id': 845,
        # en produccion PRODUCTO
        # 'product_id': 1,
        # en produccion CUENTA DE ANTICIPO
        # 'account_id': 2208,
        return res

    @api.multi
    def unlink(self):
        invoice_line = self.env['account.invoice.line'].search([('invoice_id', '=', self.id)])
        if invoice_line:
            for line in invoice_line:
                sale_line = self.env['sale.order.line'].search([('id', '=', line.blm_sale_line_ids.id)])
                if line.quantity < 0:
                    if sale_line:
                        if sale_line.blm_payment_acumulado > 0:
                            acumulado_actualizado = sale_line.blm_payment_acumulado + (line.quantity * line.price_unit)
                            sale_line.write({'blm_payment_acumulado': acumulado_actualizado})
        return super(AccountInvoice, self).unlink()


class Task(models.Model):
    _inherit = "project.task"

    sincargo_hours = fields.Float("Horas Sin Cargo", compute='_compute_sincargo_hours', compute_sudo=True, store=True)
    blm_odoo8 = fields.Char(string='Id Odoo 8 Proyecto')

    @api.depends('timesheet_ids.unit_amount')
    def _compute_sincargo_hours(self):
        for task in self:
            task.sincargo_hours = round(sum(task.timesheet_ids.filtered(lambda l: l.timesheet_invoice_type == 'non_billable').mapped('unit_amount')), 2)


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    @api.multi
    def write(self, values):
        res = super(HelpdeskTicket, self).write(values)
        if "blm_sincargo" in values.keys():
            if values['blm_sincargo'] == True:
                line_ticket = self.env['account.analytic.line'].search([('helpdesk_ticket_id', '=', self.id)])
                if line_ticket:
                    for line in line_ticket:
                        if line.timesheet_invoice_type == 'billable_time':
                            line.write({'timesheet_invoice_type': 'non_billable'})
            if values['blm_sincargo'] == False:
                line_ticket = self.env['account.analytic.line'].search([('helpdesk_ticket_id', '=', self.id)])
                if line_ticket:
                    for line in line_ticket:
                        if line.timesheet_invoice_type == 'non_billable':
                            line.write({'timesheet_invoice_type': 'billable_time'})

        if "blm_incidencia_padre" in values.keys():
            if values['blm_incidencia_padre']:
                actualiza_msj = self.env['mail.message'].search([('res_id', '=', self.id), ('model', '=', 'helpdesk.ticket')])
                if actualiza_msj:
                    for control in actualiza_msj:
                        control.write({'res_id': values['blm_incidencia_padre']})
        return res

    @api.model
    def _default_solicitud(self):
        actual = datetime.now() + timedelta(hours=1)
        actual = format(actual, "%Y%m%d%H%M%S")
        return actual

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=10000):
        res = super(HelpdeskTicket, self).name_search(name, args=args, operator=operator, limit=limit)
        if self._context.get('blm_incidencia_padre'):
            ids = self.search(args + [('solicitud', 'ilike', name)], limit=limit)
            if ids:
                return ids.name_get()
            else:
                return res
        else:
            return res

    @api.multi
    def name_get(self):
        result = []
        for ticket in self:
            if isinstance(ticket.id, int):
                result.append((ticket.id, "%s" % ticket.solicitud))
        return result


    datos ='''             SOLICITUD

            ANALISIS

            1) MODIFICACIONES MODEL

            2) MODIFICACIONES VIEW

            3) MODIFICACIONES CONTROLLER

            SOLUCION'''

    solicitud = fields.Char(string='Solicitud', default=_default_solicitud, index=True)
    blm_odoo8 = fields.Char(string='Id Odoo 8 Solicitud')
    description = fields.Text(default=datos)
    blm_sincargo = fields.Boolean(string='Sin Cargo', default=False)
    blm_incidencia_padre = fields.Many2one('helpdesk.ticket', string='Duplicada de')


    @api.onchange('project_id')
    def _onchange_blm_project(self):
        if self.project_id:
            if self.project_id.partner_id:
                self.partner_id = self.project_id.partner_id

    @api.onchange('task_id')
    def _onchange_blm_task(self):
        if self.task_id:
            if self.task_id.user_id:
                self.user_id = self.task_id.user_id



class SaleOrder(models.Model):
    _inherit = "sale.order"

    blm_odoo8 = fields.Char(string='Id Odoo 8 Pedido')
    blm_journal_id = fields.Many2one('account.journal', 'Diario', required=True, index=True, domain="[('type','=','sale')]")

    @api.multi
    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        company_id = self.company_id.id
        journal_id = self.blm_journal_id.id
        if not journal_id:
            raise UserError(_('Please define an accounting sales journal for this company.'))
        vinvoice = self.env['account.invoice'].new({'partner_id' : self.partner_invoice_id.id, 'type' : 'out_invoice'})
        # Get partner extra fields
        vinvoice._onchange_partner_id()
        invoice_vals = vinvoice._convert_to_write(vinvoice._cache)
        invoice_vals.update({
            'name': (self.client_order_ref or '')[:2000],
            'origin': self.name,
            'type': 'out_invoice',
            'account_id': self.partner_invoice_id.property_account_receivable_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'journal_id': journal_id,
            'currency_id': self.pricelist_id.currency_id.id,
            'comment': self.note,
            'payment_term_id': self.payment_term_id.id,
            'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
            'company_id': company_id,
            'user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
        })
        return invoice_vals



class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    blm_odoo8 = fields.Char(string='Id Odoo 8 Linea analitica')
    blm_odoo8_solicitud = fields.Char(string='Id Odoo 8 solicitud')
    account_id = fields.Many2one('account.analytic.account', 'Analytic Account', required=False, ondelete='restrict', index=True)


class ProjectProject(models.Model):
    _inherit = "project.project"

    blm_odoo8 = fields.Char(string='Id Odoo 8 Proyecto')


class MailMessage(models.Model):
    _inherit = "mail.message"

    blm_odoo8 = fields.Char(string='Id Odoo 8 mensaje')


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    blm_invoiced_date = fields.Date(string='Fecha Facturación')

