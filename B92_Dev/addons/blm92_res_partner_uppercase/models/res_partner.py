# -*- coding: utf-8 -*-

from odoo import models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('name')
    def _name_onchange(self):
        if (self.customer or self.supplier) and self.name:
            self.name = self.name.upper()
