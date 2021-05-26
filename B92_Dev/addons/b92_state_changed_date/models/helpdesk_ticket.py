# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    b92_last_changed_date = fields.Date(string='Último cambio de estado', readonly=True)

    b92_last_reopened_date = fields.Date(string='Fecha de la última reapertura', readonly=True)
