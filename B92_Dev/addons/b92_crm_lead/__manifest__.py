# Copyright 2015 Serv. Tec. Avanzados - Pedro M. Baeza (http://www.serviciosbaeza.com)
# Copyright 2015 AvanzOsc (http://www.avanzosc.es)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "B92 Crm Lead",
    "version": "12.0.1.0.0",
    "category": "",
    "author": "BALMES 92",
    "website": "https://balmes92.com",
    "license": "AGPL-3",
    "contributors": [
        "Eduardo Tirado <et@balmes.com>",
    ],
    "depends": ["crm_lead_code", "sale", "sale_timesheet", "sale_subscription", "account", "account_payment_partner", "helpdesk_timesheet"],
    "data": ["views/crm_lead_view.xml"],
    'installable': True,
}
