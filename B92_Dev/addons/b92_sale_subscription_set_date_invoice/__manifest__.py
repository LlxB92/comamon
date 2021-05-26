# -*- coding: utf-8 -*-
{
    'name': "B92 Facturas de Subscripción con la fecha definida",

    'summary': """
        Iguala el campo "Fecha factura" de las facturas creadas 
        con el campo "Fecha de la próxima factura" de la subscripción asociada a la factura
    """,

    'description': """
        Iguala el campo "Fecha factura" de las facturas creadas 
        con el campo "Fecha de la próxima factura" de la subscripción asociada a la factura
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_subscription'],
}
