# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': " B92 Imprimir facturas con rotura por imputación de horas",

    'summary': """
            Imprime las facturas con rotura por imputación de horas
        """,

    'description': """
            Imprime las facturas con rotura por imputación de horas
        """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    # TODO: Separar el código de las solicitudes en módulo aparte
    'depends': ['account', 'helpdesk_timesheet', 'sale_timesheet', 'b92_crm_lead'],

    "data": ["report/account_invoice_report_view.xml"],
}
