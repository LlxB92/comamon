from odoo import api, models


# noinspection PyProtectedMember
class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def _b92_write_extra_data(self, old_inv_rs):
        return {
            # Se va a permitir fusionar facturas con distintos comerciales
            # La factura resultante tendrá como comercial el user_id #1
            # En el manual se va a especificar que esto se puede cambiar manualmente.
            'user_id': 1,
            # Siempre debe coger la posición fiscal del cliente.
            'fiscal_position_id': self.partner_id.property_account_position_id.id,
        }

    @api.model
    def _get_invoice_key_cols(self):
        invoice_key_cols = super(AccountInvoice, self)._get_invoice_key_cols()

        # Se va a permitir fusionar facturas con distintos comerciales
        # La factura resultante tendrá como comercial el user_id #1
        # En el manual se va a especificar que esto se puede cambiar manualmente.
        invoice_key_cols.remove('user_id')

        return invoice_key_cols

    @api.model
    def _get_invoice_line_key_cols(self):
        return super(AccountInvoice, self)._get_invoice_line_key_cols() + [
            'purchase_line_id'
        ]

    @api.multi
    def do_merge(self, keep_references=True, date_invoice=False, remove_empty_invoice_lines=True):
        # En el ancestro de esta función se borra la relación entre las líneas de facturas y las líneas de pedidos
        # Esta información no debe de perderse
        invoices_sales_ids = {
            inv_line: inv_line.sale_line_ids.ids
            for inv in self
            for inv_line in inv.invoice_line_ids
        }

        # Si se genera(n) factura(s) fusionada(s)
        # inv_dct tendría
        #     {
        #         'ID de la factura fusionada #1': ['lista de ID de facturas que fueron fusionadas aquí'],
        #         'ID de la factura fusionada #2': ['lista de ID de facturas que fueron fusionadas aquí'],
        #     }
        inv_dct = super(AccountInvoice, self).do_merge(keep_references, date_invoice, remove_empty_invoice_lines)

        # Restaurar entre las líneas de facturas y las líneas de pedidos
        for inv_line, sale_lines_id in invoices_sales_ids.items():
            inv_line.write({'sale_line_ids': [(4, sale_line_id) for sale_line_id in sale_lines_id]})

        # Escribir datos extras
        for new_inv_id, old_inv_ids in inv_dct.items():
            new_inv = self.env['account.invoice'].browse([new_inv_id])
            old_inv_rs = self.env['account.invoice'].browse(old_inv_ids)
            old_inv_line_rs = old_inv_rs.mapped('invoice_line_ids')

            new_inv.write(new_inv._b92_write_extra_data(old_inv_rs))

            for inv_line in new_inv.invoice_line_ids:
                inv_line.write(inv_line._b92_write_extra_data(old_inv_line_rs))

        return inv_dct


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.multi
    def _b92_write_extra_data(self, old_inv_line_rs) -> dict:
        return dict()
