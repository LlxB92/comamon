from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    b92_iep = fields.Boolean(
        string='Imprimir en IEP',
        default=True,
    )


