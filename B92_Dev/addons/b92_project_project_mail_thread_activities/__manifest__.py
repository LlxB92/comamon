# -*- coding: utf-8 -*-
{
    'name': "B92 Conversaciones y Mensajes en Proyectos",

    'summary': """
        Añade la funcionalidad de mensajes y actividades en Proyectos
    """,

    'description': """
        Añade la funcionalidad de mensajes y actividades en Proyectos
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        'views/project_views.xml',
    ],
}
