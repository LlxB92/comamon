# Copyright 2016 Tecnativa - Jairo Llopis <jairo.llopis@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, exceptions, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    event_registration_id = fields.Many2one(
        comodel_name='event.registration',
        string='Event registration',
        readonly=True,
        help='Registration generated by this lead/opportunity.')

    @api.multi
    def action_generate_event_registration(self, event):
        """Generate an event registration."""
        er = self.env["event.registration"]
        for s in self:
            name = (s.contact_name or
                    s.partner_name or
                    s.partner_id.name)
            if not name:  # pragma: no cover
                raise exceptions.ValidationError(
                    _("You must set a name before generating a registration."))
            s.event_registration_id = er.create({
                "event_id": event.id,
                "partner_id": s.partner_id.id,
                "name": name,
                "email": s.email_from,
                "phone": s.phone,
            })
            # Load data from partner if available
            s.event_registration_id._onchange_partner()

    @api.multi
    def action_check_status_confirm_registration(self):
        """If the opportunity is won/lost, open/cancel registration."""
        for s in self:
            if self._track_subtype(['stage_id']) == "crm.mt_lead_won":
                s.event_registration_id.confirm_registration()
            elif self._track_subtype(['active']) == "crm.mt_lead_lost":
                s.event_registration_id.button_reg_cancel()

    @api.model
    def create(self, vals):
        result = super(CrmLead, self).create(vals)
        result.action_check_status_confirm_registration()
        return result

    @api.multi
    def write(self, vals):
        result = super(CrmLead, self).write(vals)
        self.action_check_status_confirm_registration()
        return result
