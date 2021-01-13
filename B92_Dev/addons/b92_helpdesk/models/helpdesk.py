# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _

class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    blm_time_total = fields.Float('Horas Totales Solicitud', compute='_compute_blm_total_timesheet', store=True, default=0)
    blm_hse = fields.Float('HSE', default=0)

    @api.depends('timesheet_ids')
    def _compute_blm_total_timesheet(self):
        for ticket in self:
            control = 0
            if ticket.timesheet_ids:
                for tick in ticket.timesheet_ids:
                    control = control + tick.unit_amount
                ticket.blm_time_total = control
                print(control)

