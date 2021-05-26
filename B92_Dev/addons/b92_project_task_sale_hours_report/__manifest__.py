# -*- coding: utf-8 -*-
{
    'name': "B92 Ver informe con detalle de horas e imputaciones desde Ventas",

    'summary': """
        Permite ver el que reporte detalla las horas en una tarea y sus imputaciones desde Ventas.
    """,

    'description': """
       Permite ver el que reporte detalla las horas en una tarea y sus imputaciones desde Ventas.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Project Management",
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['b92_project_task_hours_report', 'sale_timesheet'],

    # always loaded
    'data': [
        'report/sale_report_view.xml',
        'views/product_views.xml'
    ],
}
