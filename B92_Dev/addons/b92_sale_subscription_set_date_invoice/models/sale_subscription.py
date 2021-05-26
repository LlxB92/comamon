# -*- coding: utf-8 -*-

from odoo import models


# noinspection PyProtectedMember
class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    def _prepare_invoice_data(self):
        res = super(SaleSubscription, self)._prepare_invoice_data()
        res.update(date_invoice=self.recurring_next_date)
        return res
