# -*- coding: utf-8 -*-
{
    'name': "Ocultar diarios en el dashboard ",

    'summary': """
        Permite ocultar diarios en el dashboard especificados por el administrador.
    """,

    'description': """
        Permite ocultar diarios  en el dashboard especificados por el administrador.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'security/groups.xml',
        'data/config_parameter_journal_hide.xml',
        'views/account_journal_dashboard_view.xml',
    ],
}
