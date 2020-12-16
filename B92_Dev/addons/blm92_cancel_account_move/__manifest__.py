# -*- coding: utf-8 -*-
{
    'name': "Rol para la cancelación de asientos en diarios.",

    'summary': """
        Crea un rol para controlar que usuario puede cancelar asientos contables en los diarios.
    """,

    'description': """
        Crea un rol para controlar que usuario puede cancelar asientos contables en los diarios.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['account_cancel'],

    # always loaded
    'data': [
        'security/res_groups.xml',
    ],
}
