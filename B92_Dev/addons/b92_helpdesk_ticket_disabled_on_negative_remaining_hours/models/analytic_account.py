# -*- coding: utf-8 -*-

from odoo import models, api
from odoo.exceptions import UserError


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.model_create_multi
    def create(self, vals_list):
        for task in self.env['project.task'].browse([
            analytic_line_dct['task_id']
            for analytic_line_dct in vals_list
            if 'task_id' in analytic_line_dct
        ]):
            if task.b92_prepaid and task.remaining_hours < 0:
                raise UserError(f'La tarea {task.name} no tiene horas disponibles')

        return super(AccountAnalyticLine, self).create(vals_list)
