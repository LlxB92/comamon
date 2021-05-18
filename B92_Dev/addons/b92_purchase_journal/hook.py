from collections import defaultdict

from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})

    # Buscar los PO asociados a facturas no canceladas.
    po_rs = env['purchase.order'].search([
        ('invoice_ids', '!=', False)
    ]).filtered(lambda inv: inv.state != 'cancel')

    # Asociar el diario de la factura al PO
    for po in po_rs:
        inv_journal_ids = po.mapped('invoice_ids.journal_id')
        if inv_journal_ids:
            po.b92_journal_id = inv_journal_ids[0]
