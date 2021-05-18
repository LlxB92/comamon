# -*- coding: utf-8 -*-

from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    b92_journal_id = fields.Many2one(
        'account.journal', string='Diario', default=False, index=True, oldname='blm_journal_id',
        domain="[('type','=','purchase'),('company_id', '=', company_id)]", states={'draft': [('readonly', False)]}
    )
