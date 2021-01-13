# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    amount_tax_signed = fields.Monetary(string='Tax in Invoice Currency', currency_field='currency_id',
                                        readonly=True, store="True", compute='_compute_sign_taxes')
    amount_untaxed_invoice_signed = fields.Monetary(string='Untaxed Amount in Invoice Currency',
                                                    currency_field='currency_id', readonly=True,
                                                    store="True", compute='_compute_sign_taxes')

