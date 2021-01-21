from odoo import models, api


# noinspection PyProtectedMember
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        res['account_id'] = self.order_id.blm_journal_id.default_debit_account_id.id
        return res
