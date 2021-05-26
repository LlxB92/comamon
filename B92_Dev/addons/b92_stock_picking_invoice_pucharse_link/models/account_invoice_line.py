from odoo import models, api
from odoo.tools import float_compare


# noinspection PyProtectedMember
class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.multi
    def _b92_get_stock_moves_link_invoice(self):
        return self.mapped('purchase_line_id.move_ids').filtered(
            lambda x: (
                x.state == 'done'
                and not any(
                    inv.state != 'cancel'
                    for inv in x.invoice_line_ids.mapped('invoice_id')
                )
                and not x.scrapped and (
                        x.location_id.usage == 'supplier'
                        or (x.location_dest_id.usage == 'supplier' and x.to_refund)
                )
            )
        )

    @api.multi
    def _b92_link_invoices_with_pickings(self):
        # Seleccionar líneas de albaranes que:
        #   Están procesadas (estado = Hecho)
        #   No tienen asociadas facturas abiertas ni pagadas
        #   No son desechos
        #   Provienen del proveedor o si son una devolución tienen como destino el proveedor
        stock_moves = self._b92_get_stock_moves_link_invoice()

        if stock_moves:
            # Cuando se está facturando albaranes de devolución
            if float_compare(self.quantity, 0.0, precision_rounding=self.currency_id.rounding) < 0:
                stock_moves = stock_moves.filtered(
                    lambda m: m.to_refund and not m.invoice_line_ids
                )

            # Asociación entre las líneas de facturas y albaranes
            self.write({'move_line_ids': [(4, m.id) for m in stock_moves]})

            # Asociación entre las cabeceras de facturas y albaranes
            stock_moves.mapped('picking_id').write({'invoice_ids': [(4, self.invoice_id.id)]})

    @api.model_create_multi
    def create(self, vals_list):
        inv_line_rs = super(AccountInvoiceLine, self).create(vals_list)
        for line in inv_line_rs.filtered(
            lambda inv: inv.invoice_type in ('in_invoice', 'in_refund')
        ):
            line._b92_link_invoices_with_pickings()

        return inv_line_rs

    def _set_additional_fields(self, invoice):
        if invoice.type in ('in_invoice', 'in_refund'):
            # Líneas de albaranes que:
            #   Están procesadas (estado = Hecho)
            #   No tienen asociadas facturas abiertas ni pagadas
            #   No son desechos
            #   Provienen del proveedor o si son una devolución tienen como destino el proveedor
            stock_moves = self._b92_get_stock_moves_link_invoice()

            if stock_moves:
                # Cuando se está facturando albaranes de devolución
                if float_compare(self.quantity, 0.0, precision_rounding=self.currency_id.rounding) < 0:
                    stock_moves = stock_moves.filtered(
                        lambda m: m.to_refund and not m.invoice_line_ids
                    )

                # Asociación entre las líneas de facturas y albaranes
                self.move_line_ids |= stock_moves

                # Asociación entre las cabeceras de facturas y albaranes
                invoice.picking_ids |= stock_moves.mapped('picking_id')

            super(AccountInvoiceLine, self)._set_additional_fields(invoice)
