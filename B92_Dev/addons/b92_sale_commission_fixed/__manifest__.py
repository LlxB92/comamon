# -*- coding: utf-8 -*-
{
    'name': "B92 Arreglos del módulo de Comisiones",

    'summary': """
        Arregla errores de este módulo en Odoo12E
    """,

    'description': """
        Asigna el estado correcto cuando se borra una factura de liquidación de comisiones sin antes cancelarla.
        Evita error de cache en Odoo12E, cuando se borra una línea de SO, con comisión
         y se crea una nueva al mismo tiempo, con comisión.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['sale_commission'],
}
