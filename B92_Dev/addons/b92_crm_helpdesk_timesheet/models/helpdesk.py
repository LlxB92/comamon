# -*- coding: utf-8 -*-

from odoo import models, fields


class HelpdeskTicket(models.Model):
    # Private attributes
    _inherit = 'helpdesk.ticket'

    # Fields declaration
    b92_opportunity_id = fields.Many2one('crm.lead', string='Oportunidad', domain="[('type', '=', 'opportunity')]")

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides

    # Action methods

    # Business methods
