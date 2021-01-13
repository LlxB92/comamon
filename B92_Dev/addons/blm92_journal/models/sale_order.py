# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

# noinspection PyProtectedMember
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    blm_journal_id = fields.Many2one('account.journal', string='Diario', default=False, index=True, required=True,
                                     domain="[('type','=','sale'),('company_id', '=', company_id)]",
                                     states={'draft': [('readonly', False)]})

    @api.multi
    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        company_id = self.company_id.id
        journal_id = self.blm_journal_id.id
        if not journal_id:
            raise UserError(_('Please define an accounting sales journal for this company.'))
        # noinspection SpellCheckingInspection
        vinvoice = self.env['account.invoice'].new({'partner_id': self.partner_invoice_id.id, 'type': 'out_invoice'})
        # Get partner extra fields
        # noinspection PyProtectedMember
        vinvoice._onchange_partner_id()
        # noinspection PyProtectedMember,SpellCheckingInspection
        invoice_vals = vinvoice._convert_to_write(vinvoice._cache)
        invoice_vals.update({
            'name': (self.client_order_ref or '')[:2000],
            'origin': self.name,
            'type': 'out_invoice',
            'account_id': self.partner_invoice_id.property_account_receivable_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'journal_id': journal_id,
            'currency_id': self.pricelist_id.currency_id.id,
            'comment': self.note,
            'payment_term_id': self.payment_term_id.id,
            'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
            'company_id': company_id,
            'user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
        })
        return invoice_vals
