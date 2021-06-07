# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    'name': 'B92 Imprimir facturas con rotura por imputación de horas',
    'version': '12.0.1.0.0',
    'summary': 'Imprime las facturas con rotura por imputación de horas',
    'description': 'Imprime las facturas con rotura por imputación de horas',
    'category': 'Invoicing Management',
    'author': 'Balmes92',
    'company': 'Balmes92',
    'contributors':  ['Juan Carlos Fdez Hdez <jc@balmes92.com>'],
    'website': 'https://www.balmes92.com',
    'depends': ['account', 'helpdesk_timesheet', 'sale_timesheet', 'b92_helpdesk_ticket_datetime_code'],
    'data': ['report/account_invoice_report_view.xml'],
    'installable': True,
    'auto_install': False,
}
