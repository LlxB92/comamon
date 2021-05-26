# -*- coding: utf-8 -*-

from odoo import models, fields


class CrmLeadAssessmentVal(models.Model):
    # Private attributes
    _name = 'b92.crm.assessment.val'
    _description = 'Define los valores de los parámetros de la valoración'
    _rec_name = 'b92_name'
    _sql_constraints = [
        (
            'b92_param_name_uniq', 'UNIQUE (b92_param_id, b92_name)',
            'Los nombres de los valores de los parámetros para las valoraciones deben de ser únicos'
        )
    ]
    _order = 'b92_param_id, b92_value'

    # Fields declaration
    b92_name = fields.Char(string='Nombre', required=True)
    b92_value = fields.Float(string='Valor', digits=(16, 2), required=True, default=0.0)

    b92_param_id = fields.Many2one('b92.crm.assessment.param', string='Parámetro', required=True, ondelete='cascade')
    b92_assessment_val_ids = fields.Many2many(
        'crm.lead', relation='b92_crm_assessment_param_rel',
        column1='b92_assessment_val_id', column2='crm_lead_id',
        string='Valoraciones'
    )

    b92_unique = fields.Boolean(string='Excluyente', required=True, default=True, related='b92_param_id.b92_unique')

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides

    # Action methods

    # Business methods
