# -*- coding: utf-8 -*-

from odoo import models, fields


class Picking(models.Model):
    _inherit = "stock.picking"

    partner_ref = fields.Char(
        string='Referencia del albarán del proveedor', copy=False,
        oldname='x_studio_albarn_proveedor', help="Aquí podemos indicar la referencia del albarán del proveedor",
    )
