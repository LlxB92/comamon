# -*- coding: utf-8 -*-
from odoo.exceptions import UserError
from odoo import api, models, fields


class BlmInvoiceTimeSheet(models.TransientModel):
    _name = "blm.invoice.time.sheet"
    _inherit = "sale.advance.payment.inv"

    _description = "Balmes92 Invoice Timesheets"

    @api.model
    def _account_analytic_to_invoice(self):
        # Lineas seleccionadas por el usuario
        timesheet_ids = self.env['account.analytic.line'].browse(self._context.get('active_ids', []))

        # De los partes de horas seleccionados por el cliente
        # Estos son que no han sido facturados
        blm92_account_analytic_line2invoice = timesheet_ids.filtered(
            lambda timesheet: not timesheet.timesheet_invoice_id
        )

        # Estos son los partes de horas ya facturados.
        inv_timesheet_ids = timesheet_ids - blm92_account_analytic_line2invoice

        # Si el usuario selecciono partes de horas facturados
        # Entonces mostrar error
        if inv_timesheet_ids:
            raise UserError(
                'Debe deseleccionar los siguientes partes de horas facturados: \n'
                '{}'.format('\n'.join(inv_timesheet_ids.mapped('display_name')))
            )

        # Poner en active_ids los pedidos de venta asociados
        # a las lineas de partes de horas seleccionadas por el cliente
        sale_ids = timesheet_ids.mapped('so_line.order_id').ids

        return dict(
            active_ids=sale_ids, active_id=sale_ids[0],
            # Creamos esta llave dentro del context que contiene los ids de
            # las lineas de partes de horas seleccionadas por el cliente
            blm92_account_analytic_line2invoice=blm92_account_analytic_line2invoice.ids
        )

    @api.model
    def _get_advance_payment_method(self):
        # Retornar al flujo original
        # noinspection PyProtectedMember
        return super(
            # Actualizar el contexto con los albaranes a facturar dentro de sus respectivos pedidos de ventas
            # La actualización del contexto tiene que ser de esta forma, de lo contrario entra en un bucle infinito
            BlmInvoiceTimeSheet, self.with_context(
                **self._account_analytic_to_invoice()
            )
        )._get_advance_payment_method()

    # Aquí sobreescribimos el campo advance_payment_method y quitamos los métodos de pago deposito
    advance_payment_method = fields.Selection([
        ('delivered', 'Invoiceable lines'),
        ('all', 'Invoiceable lines (deduct down payments)'),
    ], default=_get_advance_payment_method)

    @api.multi
    def create_invoices(self):
        # Retornar al flujo original
        return super(
            # Actualizar el contexto con los albaranes a facturar dentro de sus respectivos pedidos de ventas
            # La actualización del contexto tiene que ser de esta forma, de lo contrario entra en un bucle infinito
            BlmInvoiceTimeSheet, self.with_context(
                **self._account_analytic_to_invoice()
            )
        ).create_invoices()


