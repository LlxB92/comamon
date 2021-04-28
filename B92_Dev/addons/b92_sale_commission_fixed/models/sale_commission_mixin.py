# -*- coding: utf-8 -*-
# Evita error de cache cuando se borra una línea de SO y se crea una nueva al mismo tiempo.

from odoo import api, fields, models


class SaleCommissionMixin(models.AbstractModel):
    _inherit = 'sale.commission.mixin'

    commission_free = fields.Boolean(
        related=False,
        compute='_compute_commission_free',
    )

    @api.multi
    @api.depends('product_id.commission_free')
    def _compute_commission_free(self):
        for line in self.filtered('product_id'):
            line.commission_free = line.product_id.commission_free
