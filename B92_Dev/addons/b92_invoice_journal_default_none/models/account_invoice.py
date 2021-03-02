# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    journal_id = fields.Many2one('account.journal', default=False)
