from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, registry):
    tracking_rs = Environment(cr, SUPERUSER_ID, {})['mail.tracking.value']

    tracking_rs.b92_set_dates(tracking_rs.b92_get_msgs_with_changed_ticket_stage().b92_get_ticket_ids())
