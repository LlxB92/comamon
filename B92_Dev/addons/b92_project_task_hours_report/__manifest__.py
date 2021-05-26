# -*- coding: utf-8 -*-
{
    'name': "B92 Informe con detalle de horas e imputaciones",

    'summary': """
        Crea un reporte detallando las horas en una tarea y sus imputaciones.
    """,

    'description': """
       Crea un reporte detallando las horas en una tarea y sus imputaciones.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Project Management",
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['b92_project_task_more_billable_hour_fields'],

    # always loaded
    'data': [
        'report/project_task_report_template.xml',
        'report/project_task_report_view.xml',
        'report/project_project_report_view.xml',
        'report/res_partner_report_view.xml',
        'views/project_task_views.xml'
    ],
}
