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

        # Obtenemos los partes de horas seleccionados por el usuario
        blm92_account_analytic_line2invoice = self._context.get('blm92_account_analytic_line2invoice', False)

        if blm92_account_analytic_line2invoice:
            # Por cada factura creada...
            for invoice in invoices.values():
                # Si la factura tiene asociada lineas de partes de horas
                if invoice.timesheet_ids:
                    # Por cada linea de la factura, se debe buscar los partes de hora asociados y...
                    for inv_line in invoice.invoice_line_ids:
                        timesheet_ids = inv_line.mapped(
                            'sale_line_ids.task_id.timesheet_ids'
                        ).filtered(
                            lambda timesheet: timesheet.id in blm92_account_analytic_line2invoice
                        )

                        if timesheet_ids:
                            # Actualizar las cantidades reales de horas facturadas en la linea
                            inv_line.write({
                                # Sumar las horas
                                'quantity': sum(timesheet_ids.mapped('unit_amount'))
                            })
                        else:
                            # Sino tiene partes de horas, se borra la linea en la factura
                            inv_line.unlink()
