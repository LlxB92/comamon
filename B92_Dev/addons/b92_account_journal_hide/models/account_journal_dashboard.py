from odoo import models, fields, api


class B92AccountJournal(models.Model):
    _inherit = "account.journal"

    @api.multi
    def _compute_show_on_dashboard(self):
        hide_journals = str(self.env['ir.config_parameter'].sudo().get_param('b92.hide.journals')).split(' | ')

        for journal in self:
            journal.b92_dashboard = self.user_has_groups(
                'b92_account_journal_hide.b92_group_show_journal_dashboard'
            ) or journal.name not in hide_journals

    @api.multi
    def _inverse_show_on_dashboard(self):
        hide_journals = set(str(self.env['ir.config_parameter'].sudo().get_param('b92.hide.journals')).split(' | '))

        for journal in self:
            if journal.show_on_dashboard:
                try:
                    hide_journals.remove(journal.name)
                except KeyError:
                    pass
            else:
                hide_journals.add(journal.name)

        self.env['ir.config_parameter'].sudo().set_param('b92.hide.journals', ' | '.join(hide_journals))

    b92_dashboard = fields.Boolean(
        string='Mostrar diario en el dashboard de contabilidad',
        default=True, compute='_compute_show_on_dashboard', inverse='_inverse_show_on_dashboard',
    )
