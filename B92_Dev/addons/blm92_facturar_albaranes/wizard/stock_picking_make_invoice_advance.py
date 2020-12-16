# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import UserError


class StockPickingAdvancePaymentInv(models.TransientModel):
    _name = "stock.picking.advance.payment.inv"
    _inherit = "sale.advance.payment.inv"

    _description = "Stock Picking Advance Payment Invoice"

    advance_payment_method = fields.Selection([
        ('delivered', 'Invoiceable lines'),
        ('all', 'Invoiceable lines (deduct down payments)'),
    ])

    @api.multi
    def create_invoices(self):
        # active_ids tiene los albaranes seleccionados por el cliente
        stock_pickings = self.env['stock.picking'].browse(self._context.get('active_ids', []))

        # Estas son las lineas de los albaranes seleccionados por el cliente
        blm92_stock_moves2invoice = stock_pickings.mapped('move_lines').filtered(
            lambda stock_move: (
                    stock_move.state == 'done'
                    and not (any(
                        inv.state != 'cancel'
                        for inv in stock_move.invoice_line_ids.mapped('invoice_id')
                    ))
                    and not stock_move.scrapped
                    and (
                            stock_move.location_dest_id.usage == 'customer' or
                            (stock_move.location_id.usage == 'customer' and stock_move.to_refund)
                    )
            )
        )

        # Poner en active_ids los pedidos de venta asociados a los albaranes seleccionados por el cliente
        sale_ids = stock_pickings.mapped('sale_id').ids

        # Retornar al flujo original
        return super(
            # Actualizar el contexto con los albaranes a facturar dentro de sus respectivos pedidos de ventas
            # La actualización del contexto tiene que ser de esta forma, de lo contrario entra en un bucle infinito
            StockPickingAdvancePaymentInv, self.with_context(
                active_ids=sale_ids, active_id=sale_ids[0],
                blm92_stock_moves2invoice=blm92_stock_moves2invoice
            )
        ).create_invoices()
