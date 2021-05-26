# -*- coding: utf-8 -*-
{
    'name': "B92 Define campos extras usados en la facturación de horas imputadas",

    'summary': """
        Define campos extras usados en la facturación de horas imputadas.
    """,

    'description': """
       Define campos extras usados en la facturación de horas imputadas.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Project Management",
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['hr_timesheet', 'sale_timesheet'],

    # always loaded
    'data': [
        'views/project_task_views.xml'
    ],
}
