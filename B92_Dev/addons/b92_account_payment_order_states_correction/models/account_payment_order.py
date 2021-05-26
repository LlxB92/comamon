# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountPaymentOrder(models.Model):
    _inherit = 'account.payment.order'

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('open', 'Confirmed'),
            ('generated', 'File Generated'),
            ('uploaded', 'File Uploaded'),
            ('cancel', 'Cancel'),
        ]
    )
