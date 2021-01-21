from odoo import models, api


# noinspection PyProtectedMember
class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def partner_banks_to_show(self):
        return (
            self._get_usable_mandate().partner_bank_id
            if self.payment_mode_id.payment_method_id.code in (
                'sepa_direct_debit', 'sdd'
            ) else
            super(AccountInvoice, self).partner_banks_to_show()
        )
