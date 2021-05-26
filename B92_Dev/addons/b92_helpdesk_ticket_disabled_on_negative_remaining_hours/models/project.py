from odoo import models, fields


class Task(models.Model):
    _inherit = 'project.task'

    b92_prepaid = fields.Boolean(
        'Pre-pago/Crédito',
        help="Permitir o impedir que la tarea se pueda pasar de horas"
    )
