# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    b92_doc_attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='b92_mail_compose_message_ir_attachments_object_rel',
        column1='b92_doc_attachment_id', column2='attachment_id',
        string='Documentos guardados',
    )

    @api.multi
    def get_mail_values(self, res_ids):
        res = super(MailComposeMessage, self).get_mail_values(res_ids)
        if self.b92_doc_attachment_ids.ids and self.model and len(res_ids) == 1:
            res[res_ids[0]].setdefault('attachment_ids', []).extend(
                self.b92_doc_attachment_ids.ids)
        return res
