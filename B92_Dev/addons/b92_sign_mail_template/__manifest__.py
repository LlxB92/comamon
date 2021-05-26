# -*- coding: utf-8 -*-
{
    'name': "B92 Asociar plantillas a los correos de firma de documentos",

    'summary': """
        Permite el uso de plantillas en los  correos de firma de documentos
    """,

    'description': """
        Permite el uso de plantillas en los  correos de firma de documentos
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Document Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sign'],

    # always loaded
    'data': [
        'wizard/sign_send_request_views.xml',
    ],
}
