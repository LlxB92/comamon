# -*- coding: utf-8 -*-
{
    'name': "B92 Adjuntar archivos guardados en el módulo de Documentos",

    'summary': """
        Permite adjuntar archivos guardados en el módulo de Documentos.
    """,

    'description': """
        Permite adjuntar archivos guardados en el módulo de Documentos.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Social Network',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'documents'],

    # always loaded
    'data': [
        'wizard/mail_compose_message_view.xml'
    ],
}
