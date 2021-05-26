# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.osv import expression


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.model
    def _timesheet_domain_get_invoiced_lines(self, sale_line_delivery):
        """ Get the domain for the timesheet to link to the created invoice
            :param sale_line_delivery: recordset of sale.order.line to invoice
            :return a normalized domain
        """
        # El objetivo de esta función es asociar las lineas de partes de horas con las lineas de la factura

        # El dominio original busca:
        # Aquellas lineas de partes de hora que están asociadas al pedido de venta
        # Que las lineas no tengan una factura asociada
        # Que las lineas estén asociadas a un proyecto
        # noinspection PyProtectedMember
        domain = super(AccountInvoiceLine, self)._timesheet_domain_get_invoiced_lines(sale_line_delivery)

        # Obteniendo lineas de partes de horas seleccionadas por el usuario
        b92_aal2invoice = self._context.get('b92_aal2invoice')

        # Si existen lineas seleccionadas por el usuario
        # Entonces se añaden como limitantes al dominio original
        if b92_aal2invoice:
            domain = expression.AND([domain, [('id', 'in', b92_aal2invoice)]])

        return domain
