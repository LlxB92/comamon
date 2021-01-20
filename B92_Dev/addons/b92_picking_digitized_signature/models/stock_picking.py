from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    b92_digital_signature = fields.Binary(string='Firma Digital', attachment=True)
