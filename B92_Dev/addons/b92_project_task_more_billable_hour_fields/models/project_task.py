from odoo import fields, models, api


# noinspection PyProtectedMember
class ProjectTask(models.Model):
    # Private attributes
    _inherit = 'project.task'

    # Default methods

    # Fields declaration
    b92_billed_hours = fields.Float(
        "Horas Facturadas", compute='_compute_b92_billed_hours', compute_sudo=True, store=True,
        help="Se calcula sumando las imputaciones de horas facturable que han sido facturadas."
    )

    b92_pending_billable_hours = fields.Float(
        "Horas Pendientes por Facturar", compute='_compute_b92_pending_billable_hours', compute_sudo=True, store=True,
        help="Se calcula sumando las imputaciones de horas facturables que no han sido facturadas."
    )

    b92_non_billable_hours = fields.Float(
        "Horas sin Cargo", compute='_compute_b92_non_billable_hours', compute_sudo=True, store=True,
        help="Se calcula sumando las imputaciones de horas no facturables."
    )

    b92_done_hours = fields.Float(
        "Horas Realizadas", compute='_compute_b92_done_hours', compute_sudo=True, store=True,
        help="Se calcula sumando las imputaciones de horas facturables y no facturables."
    )

    # compute and search fields, in the same order of fields declaration
    @api.multi
    @api.depends('timesheet_ids.unit_amount', 'timesheet_ids.timesheet_invoice_type')
    def _compute_b92_billed_hours(self):
        for task in self:
            task.b92_billed_hours = round(
                sum(
                    task.timesheet_ids.filtered(
                        lambda t: t.timesheet_invoice_id and t.timesheet_invoice_type == 'billable_time'
                    ).mapped('unit_amount')
                ), 2
            )

    @api.multi
    @api.depends('timesheet_ids.unit_amount', 'timesheet_ids.timesheet_invoice_type')
    def _compute_b92_pending_billable_hours(self):
        for task in self:
            task.b92_pending_billable_hours = round(
                sum(
                    task.timesheet_ids.filtered(
                        lambda t: not t.timesheet_invoice_id and t.timesheet_invoice_type == 'billable_time'
                    ).mapped('unit_amount')
                ), 2
            )

    @api.multi
    @api.depends('timesheet_ids.unit_amount', 'timesheet_ids.timesheet_invoice_type')
    def _compute_b92_non_billable_hours(self):
        for task in self:
            task.b92_non_billable_hours = round(
                sum(
                    task.timesheet_ids.filtered(
                        lambda t: t.timesheet_invoice_type == 'non_billable'
                    ).mapped('unit_amount')
                ), 2
            )

    @api.multi
    @api.depends('effective_hours', 'b92_non_billable_hours')
    def _compute_b92_done_hours(self):
        for task in self:
            task.b92_done_hours = task.effective_hours + task.b92_non_billable_hours

    @api.multi
    @api.depends('timesheet_ids.unit_amount', 'timesheet_ids.timesheet_invoice_type')
    def _compute_effective_hours(self):
        return super(ProjectTask, self)._compute_effective_hours()

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides

    # Action methods

    # Business methods
