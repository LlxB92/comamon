# -*- coding: utf-8 -*-
{
    'name': "Albarán Marca Blanca",

    'summary': """
        Permite generar un reporte albarán sin cabecera ni pie de pagina.
    """,

    'description': """
        Permite generar un reporte albarán sin cabecera ni pie de pagina.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'views/report_invoice.xml',
        'views/stock_report_views.xml'
    ],
}
