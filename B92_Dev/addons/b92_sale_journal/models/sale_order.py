# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


# noinspection PyProtectedMember
class SaleOrder(models.Model):
    _inherit = "sale.order"

    b92_journal_id = fields.Many2one(
        'account.journal', string='Diario', default=False, index=True, oldname='blm_journal_id',
        domain="[('type','=','sale'),('company_id', '=', company_id)]", states={'draft': [('readonly', False)]}
    )

    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res['journal_id'] = self.b92_journal_id.id
        return res
