from odoo import models, api


class CrmPhonecall(models.Model):
    _inherit = "crm.phonecall"

    @api.multi
    def action_make_meeting(self):
        self.ensure_one()
        res = super(CrmPhonecall, self).action_make_meeting()

        res['context']['default_opportunity_id'] = self.opportunity_id.id
        return res
