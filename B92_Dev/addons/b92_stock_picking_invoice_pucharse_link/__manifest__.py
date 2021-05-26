# -*- coding: utf-8 -*-
{
    'name': "B92 Link entre facturas de proveedor y albaranes de compra",

    'summary': """
        Permite asociar albaranes de compra a las facturas de proveedor
    """,

    'description': """
        Permite asociar albaranes de compra a las facturas de proveedor
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Warehouse Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['stock_picking_invoice_link', 'purchase_stock'],

    # always loaded
    'data': [
        'views/account_invoice_views.xml'
    ],
}
