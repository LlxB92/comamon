# -*- coding: utf-8 -*-

from odoo import models, api


# noinspection PyProtectedMember
class ReportInvoiceWithTimesheets(models.AbstractModel):
    # Private attributes
    _name = 'b92.account.report_invoice_with_timesheets'
    _description = (
        'Obtiene datos de las imputaciones de horas agrupadas por solicitud '
        'o por tareas si no tienen una solicitud asociada'
    )

    # Fields declaration

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides

    # Action methods

    # Business methods
    @api.model
    def _b92_get_report_values(self, docids, data=None):
        invoices = self._b92_get_invoices(docids)

        data.update({
            'docs': invoices,
            'b92_extra_data': self._b92_get_inv_extra_data(invoices),
        })

        return data

    @api.model
    def _b92_get_invoices(self, inv_ids):
        return self.env['account.invoice'].browse(inv_ids)

    @api.model
    def _b92_get_inv_extra_data(self, invoices):
        inv_extra_dct = dict()

        for invoice in invoices:
            inv_timesheets = invoice.timesheet_ids
            for inv_line in invoice.invoice_line_ids:
                inv_extra_dct[inv_line.id] = {
                    model: self._b92_header_lines_rs(recordset, inv_timesheets, filter_func)
                    for model, recordset, filter_func in zip(
                        ('helpdesk_ticket', 'project_task'),
                        self._get_b92_inv_lin_headers(self._b92_get_inv_lin_timesheets(inv_line, inv_timesheets)),
                        (self._b92_ht_filter_timesheets, self._b92_pt_filter_timesheets)
                    )
                }

        return inv_extra_dct

    @api.model
    def _b92_header_lines_rs(self, recordset, inv_timesheets, filter_func):
        return [
            {
                'header': record,
                'lines': filter_func(
                    record.timesheet_ids,
                    inv_timesheets,
                )
            }
            for record in recordset
        ]

    @api.model
    def _b92_ht_filter_timesheets(self, header_timesheets, inv_timesheets):
        return header_timesheets.filtered(
            lambda aal: aal in inv_timesheets and aal.helpdesk_ticket_id
        )

    @api.model
    def _b92_pt_filter_timesheets(self, header_timesheets, inv_timesheets):
        return header_timesheets.filtered(
            lambda aal: aal in inv_timesheets and not aal.helpdesk_ticket_id
        )

    @api.model
    def _b92_get_inv_lin_timesheets(self, inv_line, inv_timesheets):
        """
        Busca las imputaciones de horas asociadas a la línea de la factura.

        :param inv_line: Línea de la factura que se esta procesando
        :param inv_timesheets: Imputaciones de horas asociadas a la factura
        """
        return inv_timesheets.filtered(
            lambda aal: inv_line in aal.so_line.invoice_lines
        )

    def _get_b92_inv_lin_headers(self, timesheets):
        """
        Busca las solicitudes asociadas a la línea de la factura
        y las tareas de imputaciones sin solicitud asociada a la línea de la factura.

        :param timesheets: Imputaciones de horas asociadas a la factura
        """
        inv_lin_hts = self.env['helpdesk.ticket']
        inv_lin_tasks = self.env['project.task']

        for timesheet in timesheets:
            if timesheet.helpdesk_ticket_id:
                inv_lin_hts |= timesheet.helpdesk_ticket_id
            else:
                inv_lin_tasks |= timesheet.task_id

        return inv_lin_hts, inv_lin_tasks


# noinspection PyProtectedMember
class ReportInvoiceWithPayment(models.AbstractModel):
    # Private attributes
    _name = 'report.account.report_invoice_with_payments'
    _inherit = ['report.account.report_invoice_with_payments', 'b92.account.report_invoice_with_timesheets']

    # Fields declaration

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides

    # Action methods

    # Business methods
    @api.model
    def _get_report_values(self, docids, data=None):
        return self._b92_get_report_values(
            docids, super(ReportInvoiceWithPayment, self)._get_report_values(docids, data)
        )


# noinspection PyProtectedMember
class ReportInvoice(models.AbstractModel):
    # Private attributes
    _name = 'report.account.report_invoice'
    _inherit = ['b92.account.report_invoice_with_timesheets']

    # Fields declaration

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides

    # Action methods

    # Business methods
    @api.model
    def _get_report_values(self, docids, data=None):
        data.update({
            'doc_ids': docids,
            'doc_model': 'account.invoice',
            'docs': self.env['account.invoice'].browse(docids),
        })

        return self._b92_get_report_values(
            docids, data
        )
