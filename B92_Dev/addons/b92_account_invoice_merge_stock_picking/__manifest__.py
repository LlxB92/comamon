# -*- coding: utf-8 -*-
{
    'name': "B92 Fusión de facturas y sus respectivos albaranes asociados",

    'summary': """
        Este módulo permite fusionar facturas y sus respectivos albaranes asociados.
    """,

    'description': """
        Este módulo permite fusionar facturas y sus respectivos albaranes asociados.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Finance',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['b92_account_invoice_merge', 'stock_picking_invoice_link'],
}
