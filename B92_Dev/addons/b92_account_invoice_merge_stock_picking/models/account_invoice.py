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

        # Cada línea de la nueva factura fusionada tiene asociada las mismas lineas de ventas
        # que su predecesora, esta lógica puede usarse para asociar adecuadamente las líneas de albaranes
        for old_inv_line in old_inv_line_rs:
            if (
                    bool(self.sale_line_ids & old_inv_line.sale_line_ids)
                    or bool(self.purchase_id & old_inv_line.purchase_id)
            ):
                stock_mov_rs += old_inv_line.move_line_ids

        dct['move_line_ids'] = [(6, 0, stock_mov_rs.ids)]
        return dct
