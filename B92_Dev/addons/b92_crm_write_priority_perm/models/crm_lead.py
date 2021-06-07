from odoo import models, api, fields


class CrmLead(models.Model):
    # Private attributes
    _inherit = "crm.lead"

    # Default methods

    # Fields declaration
    priority = fields.Selection(copy=False)

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides
    @api.model
    def create(self, values):
        self._check_priority_perm(values, on_create=True)
        return super(CrmLead, self).create(values)

    @api.multi
    def write(self, values):
        self._check_priority_perm(values)
        return super(CrmLead, self).write(values)

    # Action methods

    # Business methods
    @api.model
    def _check_priority_perm(self, values, on_create=False):
        # Si el usuario no tiene permitido modificar el campo Prioridad de CRM
        # entonces se mantendrá el valor original/anterior.
        if (
                not self.user_has_groups('b92_crm_write_priority_perm.group_crm_modify_priority')
                and 'priority' in values
                and (values['priority'] != self.default_get(['priority'])['priority'] if on_create else True)
        ):
            values.pop('priority')
            self.env.user.notify_danger(
                message=(
                    'Usted no tiene permitido modificar el campo Prioridad de CRM.<br>'
                    'Se mantendrá el valor original/anterior.'
                ),
                title='Cambio del valor'
            )
