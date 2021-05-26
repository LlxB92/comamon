# -*- coding: utf-8 -*-
{
    'name': "B92 Referencia del proveedor en Albaranes.",

    'summary': """
        Permite añadir el código del proveedor en el albarán.
    """,

    'description': """
        Permite añadir el código del proveedor en el albarán.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Warehouse',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'views/stock_picking_views.xml',
    ],
}
