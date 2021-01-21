# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# noinspection PyProtectedMember
from odoo import models, _
from odoo.exceptions import UserError


# noinspection PyProtectedMember
class B92ReportAccountGeneralLedger(models.AbstractModel):
    _description = "General Ledger Report"
    _inherit = "account.general.ledger"

    def _get_account_names(self):
        b92_account_names = self.env['ir.config_parameter'].sudo().get_param(
            'b92.account.general.ledger'
        )
        return (
            str(b92_account_names).split(' | ')
            if b92_account_names else
            False
        )

    def _group_by_account_id(self, options, line_id):
        grouped_accounts = super(B92ReportAccountGeneralLedger, self)._group_by_account_id(options, line_id)
        b92_account_names = self._get_account_names()

        if not b92_account_names:
            raise UserError(_('Las cuentas en el parámetro b92.account.general.ledger no están definidas correctamente'))

        return (
            {
                account: grouped_accounts[account]
                for account in grouped_accounts
                if account.code + " " + account.name in b92_account_names
            }
            if self._context.get('b92_report_account_general_ledger') else
            grouped_accounts
        )
