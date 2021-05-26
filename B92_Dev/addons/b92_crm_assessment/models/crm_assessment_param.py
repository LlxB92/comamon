# -*- coding: utf-8 -*-

from odoo import models, fields


class CrmLeadAssessmentParam(models.Model):
    # Private attributes
    _name = 'b92.crm.assessment.param'
    _description = 'Define los parámetros de la valoración'
    _rec_name = 'b92_name'
    _sql_constraints = [
        (
            'b92_name_uniq', 'UNIQUE (b92_name)',
            'Los nombres de los parámetros para las valoraciones deben de ser únicos'
        )
    ]

    # Fields declaration
    b92_name = fields.Char(string='Nombre', required=True)
    b92_unique = fields.Boolean(string='Excluyente', required=True, default=True)

    b92_val_ids = fields.One2many(
        'b92.crm.assessment.val', 'b92_param_id', string='Valores', required=True
    )

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides

    # Action methods

    # Business methods
