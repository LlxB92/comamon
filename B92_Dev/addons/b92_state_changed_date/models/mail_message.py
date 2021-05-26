# -*- coding: utf-8 -*-
from odoo import api, models


class Message(models.Model):
    _inherit = 'mail.message'

    @api.multi
    def b92_get_ticket_ids(self):
        return list(set(
            self.sudo().filtered(
                lambda m: m.model == 'helpdesk.ticket'
            ).mapped('tracking_value_ids').filtered(
                lambda t: t.field == 'stage_id'
            ).mapped('mail_message_id.res_id')
        ))

    @api.multi
    def write(self, vals):
        res = super(Message, self).write(vals)

        # Los mensajes modificados tienen que ser solicitudes
        ticket_ids = self.b92_get_ticket_ids()
        if ticket_ids:
            # Actualizar la fecha del último cambio de estado y la fecha de última re-apertura de las solicitudes
            self.env['mail.tracking.value'].b92_set_dates(ticket_ids)

        return res

    @api.multi
    def unlink(self):
        ticket_ids = self.b92_get_ticket_ids()

        res = super(Message, self).unlink()

        # Los mensajes a borrar tienen que ser solicitudes
        if ticket_ids:
            # Actualizar la fecha del último cambio de estado y la fecha de última re-apertura de las solicitudes
            self.env['mail.tracking.value'].b92_set_dates(ticket_ids, True)

        return res
