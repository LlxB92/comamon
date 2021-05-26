# -*- coding: utf-8 -*-
{
    'name': "Facturas con Albaranes",

    'summary': """
        Crea un reporte de factura listando los albaranes.
    """,

    'description': """
       Crea un reporte de factura listando los albaranes.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['b92_stock_picking_invoice_pucharse_link', 'b92_stock_picking_partner_reference'],

    # always loaded
    'data': [
        'data/reports.xml',
    ],
}
