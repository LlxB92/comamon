# -*- coding: utf-8 -*-
{
    'name': "B92 Deshabilitar solicitudes cuando no queden horas en la tarea",

    'summary': """
        Alerta e impide la imputación de horas en solicitudes que no tengan horas disponibles en la tarea
    """,

    'description': """
        Alerta e impide la imputación de horas en solicitudes que no tengan horas disponibles en la tarea
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['helpdesk_timesheet'],

    # always loaded
    'data': [
        'views/helpdesk_views.xml',
        'views/project_task_views.xml',
    ],
}
