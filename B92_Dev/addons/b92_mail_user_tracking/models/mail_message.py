# -*- coding: utf-8 -*-
from odoo import models, api


class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.multi
    def action_form_view(self):
        self.ensure_one()
        return self.env[self.model].browse(self.res_id).get_formview_action()

    @api.model
    def create(self, values):
        if (
            values.get('model', self.env.context.get('default_model')) != 'ir.attachment'
            and not values.get('record_name', self.env.context.get('default_record_name'))
        ):
            values['record_name'] = self._get_record_name(values)

        return super(MailMessage, self).create(values)
