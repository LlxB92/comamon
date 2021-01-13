from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _finalize_invoices(self, invoices, references):
        """
        Invoked after creating invoices at the end of action_invoice_create.
        :param invoices: {group_key: invoice}
        :param references: {invoice: order}
        """
        # noinspection PyProtectedMember
        super(SaleOrder, self)._finalize_invoices(invoices, references)

        # Obtenemos los albaranes seleccionados por el usuario
        blm92_stock_moves2invoice = self._context.get('blm92_stock_moves2invoice', False)

        if blm92_stock_moves2invoice:
            # Por cada factura creada...
            for invoice in invoices.values():
                # Si la factura tiene asociada albaranes
                if invoice.picking_ids:
                    # Por cada línea de la factura, se debe buscar las líneas de albarán asociadas y...
                    for inv_line in invoice.invoice_line_ids:
                        stock_move_ids = inv_line.mapped(
                            'sale_line_ids.move_ids'
                        ).filtered(
                            lambda stock_move: stock_move.id in blm92_stock_moves2invoice.ids
                        )

                        if stock_move_ids:
                            # Actualizar las cantidades reales del producto según las líneas de los albaranes
                            inv_line.write({
                                # Sumar las horas
                                'quantity': sum(stock_move_ids.mapped('quantity_done'))
                            })
                        else:
                            # Sino tiene líneas de albarán, se borra la linea en la factura
                            inv_line.unlink()
