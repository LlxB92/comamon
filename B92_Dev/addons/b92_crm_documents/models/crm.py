# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class Lead(models.Model):
    _inherit = "crm.lead"

    attachment_number = fields.Integer(compute='_compute_attachment_number_crm', string="Number of Attachments")

    @api.multi
    def _compute_attachment_number_crm(self):
        read_group_res = self.env['ir.attachment'].read_group(
            [('res_model', '=', 'crm.lead'), ('res_id', 'in', self.ids)],
            ['res_id'], ['res_id'])
        attach_data = {res['res_id']: res['res_id_count'] for res in read_group_res}
        for record in self:
            record.attachment_number = attach_data.get(record.id, 0)

    @api.multi
    def action_get_attachment_tree_view_crm(self):
        attachment_action = self.env.ref('base.action_attachment')
        action = attachment_action.read()[0]
        action['domain'] = str(['&', ('res_model', '=', self._name), ('res_id', 'in', self.ids)])
        return action
