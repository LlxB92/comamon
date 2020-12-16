# -*- coding: utf-8 -*-

from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def get_stock_moves_link_invoice(self):
        # Obtener las líneas de los albaranes a facturar, seleccionados por el usuario, del contexto.
        blm92_stock_moves2invoice = self._context.get('blm92_stock_moves2invoice', None)
        if blm92_stock_moves2invoice:
            # Solo devolver las líneas de albarán asociadas a esta línea del pedido de venta que se está procesando
            return blm92_stock_moves2invoice.filtered(
                lambda stock_move: stock_move in self.move_ids
            )

        return super(SaleOrderLine, self).get_stock_moves_link_invoice()
