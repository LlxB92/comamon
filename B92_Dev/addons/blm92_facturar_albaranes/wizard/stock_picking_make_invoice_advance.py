# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import UserError


class StockPickingAdvancePaymentInv(models.TransientModel):
    _name = "stock.picking.advance.payment.inv"
    _inherit = "sale.advance.payment.inv"

    _description = "Stock Picking Advance Payment Invoice"

    @api.model
    def _get_advance_payment_method(self):
        # Retornar al flujo original
        # noinspection PyProtectedMember
        return super(
            # Actualizar el contexto con los albaranes a facturar dentro de sus respectivos pedidos de ventas
            # La actualización del contexto tiene que ser de esta forma, de lo contrario entra en un bucle infinito
            StockPickingAdvancePaymentInv, self.with_context(
                **self._stock_picking2sale_order()
            )
        )._get_advance_payment_method()

    advance_payment_method = fields.Selection([
        ('delivered', 'Invoiceable lines'),
        ('all', 'Invoiceable lines (deduct down payments)'),
    ], default=_get_advance_payment_method)

    def _stock_picking2sale_order(self):
        # Si ya se hizo la transformada
        # Entonces la llave blm92_stock_moves2invoice existe
        # Y no se vuelve a hacer
        if not self._context.get('blm92_stock_moves2invoice', False):
            # active_ids tiene los albaranes seleccionados por el cliente
            stock_picking_ids = self.env['stock.picking'].browse(self._context.get('active_ids', []))

            # Estos son los albaranes seleccionados por el cliente que se pueden facturar
            stock_picking2invoice_ids = stock_picking_ids.filtered('blm92_is_invoiceable')

            # Estos son los albaranes seleccionados por el cliente que ya se facturaron
            inv_stock_picking_ids = stock_picking_ids - stock_picking2invoice_ids

            # Si entre los albaranes seleccionados por el cliente hay alguno que ya esté facturado
            # Entonces lanzar error
            if inv_stock_picking_ids:
                raise UserError(
                    'Debe deseleccionar los siguientes albaranes facturados: \n'
                    '{}'.format('\n'.join(inv_stock_picking_ids.mapped('display_name')))
                )

            # Estas son las lineas de los albaranes seleccionados por el cliente
            blm92_stock_moves2invoice = stock_picking_ids.mapped('move_lines').filtered(
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
            sale_ids = stock_picking_ids.mapped('sale_id').ids

            return dict(
                active_ids=sale_ids, active_id=sale_ids[0],
                # Creamos esta llave dentro del context que contiene los ids de
                # los albaranes seleccionados por el cliente
                blm92_stock_moves2invoice=blm92_stock_moves2invoice
            )

        # Ya la transformada se hizo por lo que solo retornamos los valores
        return dict(
            active_ids=self._context.get('active_ids', False), active_id=self._context.get('active_id', False),
            blm92_stock_moves2invoice=self._context.get('blm92_stock_moves2invoice', False),
        )

    @api.multi
    def create_invoices(self):
        # Retornar al flujo original
        return super(
            # Actualizar el contexto con los albaranes a facturar dentro de sus respectivos pedidos de ventas
            # La actualización del contexto tiene que ser de esta forma, de lo contrario entra en un bucle infinito
            StockPickingAdvancePaymentInv, self.with_context(
                **self._stock_picking2sale_order()
            )
        ).create_invoices()
