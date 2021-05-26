# -*- coding: utf-8 -*-
{
    'name': "B92 Firma digital en Albaranes",

    'summary': """
        Añade un apartado para que el cliente firme digitalmente los albaranes.
    """,

    'description': """
        Añade un apartado para que el cliente firme digitalmente los albaranes.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Warehouse Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'web_widget_digitized_signature'],

    # always loaded
    'data': [
        'report/report_deliveryslip.xml',
        'report/report_stockpicking_operations.xml',

        'views/stock_picking_views.xml',
    ],
}
