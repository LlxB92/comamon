# -*- coding: utf-8 -*-
{
    'name': 'Firma digital en Albaranes',
    'version': '12.0.1.0.0',
    'summary': 'Añade un apartado para que el cliente firme digitalmente los albaranes.',
    'description': 'Añade un apartado para que el cliente firme digitalmente los albaranes.',
    'category': 'Warehouse Management',
    'author': 'Balmes92',
    'company': 'Balmes92',
    'contributors':  ['Juan Carlos Fdez Hdez <jc@balmes92.com>'],
    'website': 'https://www.balmes92.com',
    'depends': ['stock', 'web_widget_digitized_signature'],
    'data': [
        'report/report_deliveryslip.xml',
        'report/report_stockpicking_operations.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
