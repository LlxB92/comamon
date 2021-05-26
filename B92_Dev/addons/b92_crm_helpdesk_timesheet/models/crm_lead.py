# -*- coding: utf-8 -*-

from odoo import models, fields, api


# noinspection PyProtectedMember
class Lead(models.Model):
    # Private attributes
    _inherit = "crm.lead"

    # Fields declaration
    b92_helpdesk_ticket_ids = fields.One2many('helpdesk.ticket', 'b92_opportunity_id', string='Tickets')
    b92_helpdesk_ticket_count = fields.Integer(compute='_compute_b92_helpdesk_ticket_count')

    # compute and search fields, in the same order of fields declaration
    @api.depends('b92_helpdesk_ticket_ids')
    def _compute_b92_helpdesk_ticket_count(self):
        for ticket in self:
            ticket.b92_helpdesk_ticket_count = len(ticket.b92_helpdesk_ticket_ids)

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides

    # Action methods
    @api.multi
    def action_open_helpdesk_ticket(self):
        action = self.env.ref('helpdesk.helpdesk_ticket_action_main_tree').read()[0]
        action['context'] = {}
        action['domain'] = [('b92_opportunity_id', 'in', self.ids)]
        return action

    # Business methods
