# -*- coding: utf-8 -*-

{
    'name': "B92 Rastreo de las acciones de los usuarios",

    'summary': """
        Permite rastrear las acciones de los usuarios
    """,

    'description': """
        Permite rastrear las acciones de los usuarios
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['board', 'mail'],

    # always loaded
    'data': [
        'views/mail_message_views.xml',
    ],

    "post_init_hook": "post_init_hook",
}
