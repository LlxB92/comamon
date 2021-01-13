from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.depends('state', 'sale_id', 'picking_type_code', 'invoice_ids', 'invoice_ids.state')
    def _is_invoiceable(self):
        for stock_picking in self:
            # Un albarán es facturable si:
            #   Está entregado
            #   Está asociado a un pedido de venta
            #   Es un albarán de salida
            #   No tiene asociado facturas o solo tiene facturas canceladas
            stock_picking.blm92_is_invoiceable = (
                stock_picking.state == 'done'
                and bool(stock_picking.sale_id) and stock_picking.picking_type_code == 'outgoing'
                and all(state == 'cancel' for state in stock_picking.mapped('invoice_ids.state'))
            )

    # Para que se pueda filtrar por este campo hay que crearlo en la DB con store=True
    blm92_is_invoiceable = fields.Boolean(string='Es Facturable', compute='_is_invoiceable', store=True)
