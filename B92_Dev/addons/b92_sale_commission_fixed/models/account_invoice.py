# -*- coding: utf-8 -*-
# Asigna el estado correcto cuando se borra una factura de liquidación de comisiones sin antes cancelarla.

from odoo import models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def unlink(self):
        """Put settlements associated to the invoices in exception."""
        settlements = self.env['sale.commission.settlement'].search([('invoice', 'in', self.ids)])
        if settlements:
            settlements.write({'state': 'except_invoice'})
        return super(AccountInvoice, self).unlink()
