{
    "name": "B92 Facturar Horas",
    "version": "12.0.1.0.0",
    "category": "",
    "author": "BALMES 92",
    "website": "https://balmes92.com",
    "license": "AGPL-3",
    "contributors": [
        "Eduardo Arturo Tirado <et@balmes.com>",
        "Juan Carlos Fernández <et@balmes.com>",
    ],
    "depends": ["account", "sale", "hr_timesheet", "sale_timesheet"],
    "data": [
        'wizard/sale_make_invoice_advance_views.xml',
        'views/invoice_timesheet_search_view.xml',
    ],
    'installable': True,
}
