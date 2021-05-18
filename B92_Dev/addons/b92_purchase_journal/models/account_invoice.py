# -*- coding: utf-8 -*-

from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.onchange('purchase_id')
    def purchase_order_change(self):
        if self.purchase_id:
            self.journal_id = self.purchase_id.b92_journal_id

        return super().purchase_order_change()
