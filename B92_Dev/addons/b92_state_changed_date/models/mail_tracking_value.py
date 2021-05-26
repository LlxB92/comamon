# -*- coding: utf-8 -*-
from odoo import api, models


class MailTracking(models.Model):
    _inherit = 'mail.tracking.value'

    @api.multi
    def _b92_get_ticket_ids(self):
        return list(set(
            self.filtered(
                lambda t: t.field == 'stage_id'
            ).mapped('mail_message_id').filtered(
                lambda m: m.model == 'helpdesk.ticket'
            ).mapped('res_id')
        ))

    @api.model
    def _b92_get_stage_seqs(self):
        """
        Buscar todas las etapas de cierre
        :return: int
        """
        return self.env['helpdesk.stage'].search([
            ('is_close', '=', True),
        ]).mapped('sequence')

    @api.model
    def b92_get_msgs_with_changed_ticket_stage(self, ticket_ids: list = None):
        """
        Buscar los mensajes de solicitudes que reporten un cambio en el estado de la solicitud
        :return: mail.message
        """
        domain = [
            ('model', '=', 'helpdesk.ticket'),
            ('tracking_value_ids.field', '=', 'stage_id'),
        ]

        if ticket_ids:
            domain.append(('res_id', 'in', ticket_ids))

        return self.env['mail.message'].sudo().search(domain)

    @api.model
    def b92_set_dates(self, ticket_ids: list, unlink=False):
        # Buscar los mensajes de solicitudes que reporten un cambio en el estado de la solicitud
        msg_rs = self.b92_get_msgs_with_changed_ticket_stage(ticket_ids)

        # Buscar las solicitudes
        ticket_rs = self.env['helpdesk.ticket'].browse(ticket_ids)

        for ticket in ticket_rs:
            date_dct = dict()

            # Actualizar la fecha del último cambio de estado
            last_changed_datetime = max(
                msg_rs.filtered(lambda msg: msg.res_id == ticket.id).mapped('date'), default=None
            )
            if last_changed_datetime:
                date_dct['b92_last_changed_date'] = last_changed_datetime.date()
            elif unlink:
                date_dct['b92_last_changed_date'] = False

            # Actualizar la fecha de última re-apertura de la solicitud
            last_reopened_datetime = max(
                msg_rs.filtered(
                    lambda msg: msg.res_id == ticket.id and msg.tracking_value_ids.filtered(
                        lambda t: t.old_value_integer in self._b92_get_stage_seqs()
                    )
                ).mapped('date'),
                default=None
            )
            if last_reopened_datetime:
                date_dct['b92_last_reopened_date'] = last_reopened_datetime.date()
            elif unlink:
                date_dct['b92_last_reopened_date'] = False

            if date_dct:
                ticket.write(date_dct)

    @api.model_create_multi
    def create(self, vals_list):
        tracking_rs = super(MailTracking, self).create(vals_list)

        # Las líneas de mensajes creadas tienen que ser solicitudes
        ticket_ids = tracking_rs._b92_get_ticket_ids()
        if ticket_ids:
            # Actualizar la fecha del último cambio de estado y la fecha de última re-apertura de las solicitudes
            self.b92_set_dates(ticket_ids)

        return tracking_rs

    @api.multi
    def write(self, vals):
        res = super(MailTracking, self).write(vals)

        # Las líneas de mensajes modificadas tienen que ser solicitudes
        ticket_ids = self._b92_get_ticket_ids()
        if ticket_ids:
            # Actualizar la fecha del último cambio de estado y la fecha de última re-apertura de las solicitudes
            self.b92_set_dates(ticket_ids)

        return res

    @api.multi
    def unlink(self):
        ticket_ids = self._b92_get_ticket_ids()

        res = super(MailTracking, self).unlink()

        # Las líneas de mensajes a borrar tienen que ser solicitudes
        if ticket_ids:
            # Actualizar la fecha del último cambio de estado y la fecha de última re-apertura de las solicitudes
            self.b92_set_dates(ticket_ids, True)

        return res
