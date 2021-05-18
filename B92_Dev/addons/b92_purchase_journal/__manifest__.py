# -*- coding: utf-8 -*-
{
    'name': " B92 Agregar Diarios a Pedidos de Compra",

    'summary': """
        Fuerza a los usuarios a elegir un diario en PO para ser usado en la creación de facturas de proveedor.
    """,

    'description': """
        Fuerza a los usuarios a elegir un diario en PO para ser usado en la creación de facturas de proveedor.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    "data": ["views/purchase_views.xml"],

    "post_init_hook": "post_init_hook",
}
