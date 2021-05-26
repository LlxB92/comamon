# -*- coding: utf-8 -*-
{
    'name': "B92 Margen Neto en Ventas",

    'summary': """
        Margen luego de restar las comisiones
    """,

    'description': """
        Margen luego de restar las comisiones
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_commission', 'sale_margin', 'b92_percent_field'],

    # always loaded
    'data': [
        'views/sale_net_margin_view.xml',
    ],
}
