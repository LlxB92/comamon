# -*- coding: utf-8 -*-
import json

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# noinspection PyProtectedMember
class Lead(models.Model):
    # Private attributes
    _inherit = "crm.lead"

    # Fields declaration
    b92_assessment_val_ids = fields.Many2many(
        'b92.crm.assessment.val', 'b92_crm_assessment_param_rel',
        column1='crm_lead_id', column2='b92_assessment_val_id',
        string='Valoraciones', required=True,
    )

    b92_assessment = fields.Float(
        string='Valoración', required=True, digits=(16, 2), default=1.0, store=True,
        compute='_compute_b92_assessment'
    )
    b92_assessment_val_ids_domain = fields.Char(
        string='Dominio para Valoraciones',
        compute="_compute_b92_assessment",
        readonly=True,
        store=False,
    )

    # compute and search fields, in the same order of fields declaration
    @api.multi
    @api.depends('b92_assessment_val_ids', 'b92_assessment_val_ids.b92_value')
    def _compute_b92_assessment(self):
        for ld in self:
            ld.b92_assessment_val_ids_domain = json.dumps([(
                # Solo mostrar parámetros excluyentes cuyos valores no hayan sidos seleccionados
                'b92_param_id', 'not in',
                ld.mapped('b92_assessment_val_ids.b92_param_id').filtered('b92_unique').ids
            )])

            ld.b92_assessment = sum(ld.mapped('b92_assessment_val_ids.b92_value'), 0.0)

        self._check_b92_assessment()

    # Constraints and onchanges
    @api.multi
    @api.constrains('b92_assessment_val_ids')
    def _check_b92_assessment(self):
        for ld in self:
            val_rs = ld.mapped('b92_assessment_val_ids')
            if len(val_rs) > 1:
                # No se puede elegir varios valores de parámetros excluyentes
                for param_id in val_rs.mapped('b92_param_id').filtered('b92_unique').ids:
                    if len(val_rs.filtered(
                        lambda val: val.b92_param_id.id == param_id
                    )) > 1:
                        raise ValidationError('No puede elegir varios valores de parámetros excluyentes')

    # CRUD methods (and name_get, name_search, ...) overrides

    # Action methods

    # Business methods
