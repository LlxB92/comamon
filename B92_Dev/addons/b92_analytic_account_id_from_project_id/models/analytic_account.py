# -*- coding: utf-8 -*-

from odoo import models, api


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.model
    def default_get(self, field_list):
        result = super(AccountAnalyticLine, self).default_get(field_list)
        project_id = result.get('project_id')

        if not self.env.context.get('default_account_id') and 'account_id' in field_list and project_id:
            result['account_id'] = self.env['project.project'].browse(project_id).analytic_account_id.id

        return result
