# -*- coding: utf-8 -*-

from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.model
    def default_get(self, default_fields):
        res = super(AccountInvoice, self).default_get(default_fields)

        if 'journal_id' in res and res.get('state', False) == 'draft':
            del res['journal_id']

        return res
