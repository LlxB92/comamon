# -*- coding: utf-8 -*-

from odoo import models, fields, api


# noinspection PyAttributeOutsideInit
class SignSendRequest(models.TransientModel):
    _inherit = 'sign.send.request'

    b92_mail_template_id = fields.Many2one(
        # domain model debe ser = a default_model en vista XML
        'mail.template', 'Usar plantilla', index=True, domain="[('model', '=', 'sign.template')]"
    )

    @api.multi
    @api.onchange('b92_mail_template_id')
    def onchange_b92_mail_template_id(self):
        self.ensure_one()

        if self.b92_mail_template_id:
            self.message = self.env['mail.template'].with_context(tpl_partners_only=True).browse(
                self.b92_mail_template_id.id
            ).generate_email(
                res_ids=self._context.get('active_ids', False),
                fields=['body_html']
            )[self._context.get('active_id', False)]['body_html']
