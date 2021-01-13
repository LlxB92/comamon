# -*- coding: utf-8 -*-

from odoo import api, models


# noinspection PyProtectedMember
class Blm92PickingReport(models.AbstractModel):
    _name = 'report.stock.report_picking'

    @api.model
    def _get_report_values(self, docids, data=None):
        model = self.env['ir.actions.report']._get_report_from_name(
            'blm92_albaran_marca_blanca.blm92_report_marca_blanca'
        ).model

        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': self.env[model].browse(docids),
            'blm92_albaran_marca_blanca': False,
        }
