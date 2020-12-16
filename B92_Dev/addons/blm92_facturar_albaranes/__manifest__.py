# -*- coding: utf-8 -*-
{
    'name': "Facturar Albaranes",

    'summary': """
        Permite generar seleccionar albaranes y generar facturas a partir de esta selección
    """,

    'description': """
        Permite generar seleccionar albaranes y generar facturas a partir de esta selección
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['stock_picking_invoice_link'],

    # always loaded
    'data': [
        'views/invoice_from_stock_pickings.xml',
        'wizard/stock_picking_make_invoice_advance_views.xml',
    ],
}
