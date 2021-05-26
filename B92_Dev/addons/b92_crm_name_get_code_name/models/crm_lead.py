# -*- coding: utf-8 -*-

from odoo import models, api


# noinspection PyProtectedMember
class Lead(models.Model):
    # Private attributes
    _inherit = "crm.lead"

    # Fields declaration

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if not (name == '' and operator == 'ilike'):
            args += ['|', ('code', 'ilike', name)]

        return super(Lead, self)._name_search(name, args, operator, limit, name_get_uid)

    @api.multi
    def name_get(self):
        return [
            (ld.id, f'{ld.code} {ld.name}'.strip())
            for ld in self
            if isinstance(ld.id, int)
        ]

    # Action methods

    # Business methods
