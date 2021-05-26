# -*- coding: utf-8 -*-
{
    'name': "B92 SAT Fechas de cambio de estados",

    'summary': """
        Muestra en un campo la fecha del último cambio de estado y la fecha de última re-apertura.  
    """,

    'description': """
        Muestra en un campo la fecha del último cambio de estado y la fecha de última re-apertura.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['helpdesk', 'b92_crm_lead'],

    "post_init_hook": "post_init_hook",
}
