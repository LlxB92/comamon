from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    b92_iep = fields.Boolean(
        string='Imprimir en IEP',
        default=True,
    )
