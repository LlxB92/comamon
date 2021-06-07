# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from odoo import models, api, fields


# noinspection PyProtectedMember
class HelpdeskTicket(models.Model):
    # Private attributes
    _inherit = "helpdesk.ticket"

    # Default methods
    @api.model
    def _default_b92_number(self):
        return format(datetime.now() + timedelta(hours=1), "%Y%m%d%H%M%S")

    # Fields declaration
    b92_number = fields.Char(
        string='Solicitud', default=_default_b92_number,
        readonly=False, oldname='solicitud',
    )

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if not (name == '' and operator == 'ilike'):
            args = ['|', ('b92_number', 'ilike', name)]

        return super(HelpdeskTicket, self)._name_search(name, args, operator, limit, name_get_uid)

    @api.multi
    def name_get(self):
        result = []
        for ticket in self:
            if ticket.b92_number:
                result.append((ticket.id, f"{ticket.b92_number} {ticket.name}"))
        return result

    # Action methods

    # Business methods
