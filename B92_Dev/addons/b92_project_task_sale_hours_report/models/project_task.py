from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    b92_iep = fields.Boolean(
        string='Imprimir en IEP',
        related='sale_line_id.product_id.product_tmpl_id.b92_iep',
        store=True,
    )
