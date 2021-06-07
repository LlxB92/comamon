# -*- coding: utf-8 -*-
{
    'name': "B92 Mostrar prioridad en vista lista de CRM",

    'summary': """
        Muestra la prioridad en vista lista de CRM.
    """,

    'description': """
        Muestra la prioridad en vista lista de CRM.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        'views/crm_lead_views.xml',
    ],
}
