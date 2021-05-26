# -*- coding: utf-8 -*-

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends('commission_total', 'margin')
    def _b92_compute_net_margin(self):
        for sale in self:
            sale.b92_net_margin = sale.margin - sale.commission_total
            sale.b92_net_margin_percent = (
                (sale.b92_net_margin or 0.0) / sale.amount_untaxed * 100 if sale.amount_untaxed > 0.0 else 0.0
            )

    b92_net_margin = fields.Float(
        string="Margen Neto",
        compute="_b92_compute_net_margin",
        store=True,
    )

    b92_net_margin_percent = fields.Float(
        string=" % del Margen Neto",
        compute="_b92_compute_net_margin",
        store=True,
        digits=(16, 2),
    )
