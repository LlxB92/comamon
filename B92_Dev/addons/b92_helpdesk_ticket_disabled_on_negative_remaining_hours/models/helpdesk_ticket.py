# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    b92_remaining_hours = fields.Float(
        "Horas disponibles", related='task_id.remaining_hours', readonly=True,
        help="Tiempo restante total"
    )

    b92_prepaid = fields.Boolean(
        'Pre-pago/Crédito', related='task_id.b92_prepaid', readonly=True,
        help="Permitir o impedir que la tarea se pueda pasar de horas"
    )
