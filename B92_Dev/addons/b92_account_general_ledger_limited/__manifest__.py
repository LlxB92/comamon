# -*- coding: utf-8 -*-
{
    'name': "B92 Informe de auditoría de libro mayor limitado",

    'summary': """
        Muestra un informe limitado de auditoría de libro mayor.
    """,

    'description': """
        Muestra un informe limitado de auditoría de libro mayor.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['account_reports'],

    # always loaded
    'data': [
        'data/account_financial_report_data.xml',
    ],
}
