from odoo import api, models


# noinspection PyProtectedMember
class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def _b92_write_extra_data(self, old_inv_rs):
        dct = super(AccountInvoice, self)._b92_write_extra_data(old_inv_rs)
        # Asociar las cabeceras de albarán
        picking_ids = old_inv_rs.mapped('picking_ids').ids
        if picking_ids:
            dct['picking_ids'] = [(6, 0, picking_ids)]

        return dct


# noinspection PyProtectedMember
class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.multi
    def _b92_write_extra_data(self, old_inv_line_rs) -> dict:
        dct = super(AccountInvoiceLine, self)._b92_write_extra_data(old_inv_line_rs)

        # Asociar las líneas de albarán a las líneas de la nueva factura fusionada
        stock_mov_rs = self.env['stock.move']

        for old_inv_line in old_inv_line_rs:
            if (
                    # Cada línea de la nueva factura de venta fusionada tiene asociada las mismas lineas de ventas
                    # que su predecesora, esta lógica puede usarse para asociar adecuadamente las líneas de albaranes
                    (
                        bool(self.sale_line_ids & old_inv_line.sale_line_ids)
                        and self.invoice_type in ('out_invoice', 'out_refund')
                    )
                    # Para el caso de una facturas de proveedor fusionada la única opción es revisar lo siguiente:
                    # si todos los campos involucrados en la fusión son iguales
                    # entonces asociar las líneas de albaranes
                    or (
                        all(
                            self.mapped(field) == old_inv_line.mapped(field)
                            for field in self.invoice_id._get_invoice_line_key_cols()
                        ) and self.invoice_type in ('in_invoice', 'in_refund')
                    )
            ):
                stock_mov_rs |= old_inv_line.move_line_ids

        dct['move_line_ids'] = [(6, 0, stock_mov_rs.ids)]
        return dct
