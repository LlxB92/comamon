# -*- coding: utf-8 -*-
{
    'name': "B92 Arreglos al módulo de llamadas telefónicas de la OCA",

    'summary': """
        Arregla errores de este módulo en Odoo12E
    """,

    'description': """
        Elimina el error SQL cuando se crea una llamada a partir del wizard "Planificar otra llamada".
        Asocia las reuniones creadas a partir de una llamada asociada a un LD a la LD en cuestión.
    """,

    'author': "Juan Carlos Fernández",
    'website': "https://www.balmes92.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customer Relationship Management',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['crm_phonecall'],
}
