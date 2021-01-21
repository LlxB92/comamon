# -*- coding: utf-8 -*-
{
    'name': "B92 Mandato de adeudo directo en facturas",

    'summary': """
        Permite imprimir la cuenta bancaria de los mandatos de Odoo Enterprise empleando los módulos de de la OCA.
    """,

    'description': """
        Permite imprimir la cuenta bancaria de los mandatos de Odoo Enterprise empleando los módulos de de la OCA.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['account_payment_partner', 'account_sepa_direct_debit'],
}
