# -*- coding: utf-8 -*-
{
    'name': "B92 Valoraciones en Iniciativas/Oportunidades",

    'summary': """
        Permite implementar valoraciones en iniciativas/oportunidades.
    """,

    'description': """
        Permite implementar valoraciones en iniciativas/oportunidades.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['crm', 'web_domain_field'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/crm_assessment_views.xml',
        'views/crm_assessment_param_views.xml',
        'views/crm_assessment_val_views.xml',
        'views/crm_lead_views.xml',
    ],
}
