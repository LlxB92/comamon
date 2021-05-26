from odoo import fields, models, api


# noinspection PyProtectedMember
class AccountInvoice(models.Model):
    # Private attributes
    _inherit = "account.invoice"

    # Default methods

    # Fields declaration
    b92_digital_signature = fields.Binary(string='Firma Digital', attachment=True, copy=False)

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides
    @api.model
    def create(self, values):
        inv = super(AccountInvoice, self).create(values)
        if inv.b92_digital_signature:
            values = {'b92_digital_signature': inv.b92_digital_signature}
            inv._track_signature(values, 'b92_digital_signature')
        return inv

    @api.multi
    def write(self, values):
        self._track_signature(values, 'b92_digital_signature')
        return super(AccountInvoice, self).write(values)

    # Action methods

    # Business methods
