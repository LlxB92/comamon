# -*- coding: utf-8 -*-

from odoo import api, models


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
        blm92_account_analytic_line2invoice = self._context.get('blm92_account_analytic_line2invoice', False)

        # Si existen lineas seleccionadas por el usuario
        # Entonces se añaden como limitantes al dominio original
        if blm92_account_analytic_line2invoice:
            domain.append(('id', 'in', self._context.get('blm92_account_analytic_line2invoice', False)))

        return domain
