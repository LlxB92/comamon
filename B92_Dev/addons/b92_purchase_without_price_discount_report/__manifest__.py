# -*- coding: utf-8 -*-
{
    'name': "B92 Informe de Pedido de Compra (Sin precio ni descuento)",

    'summary': """
        Crea un reporte similar a "Pedido de Compra" (Sin precio ni descuento).
    """,

    'description': """
       Crea un reporte similar a "Pedido de Compra" (Sin precio ni descuento).
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Purchases",
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        'data/reports.xml',
    ],
}
