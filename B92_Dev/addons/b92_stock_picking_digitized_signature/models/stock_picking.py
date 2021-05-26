from odoo import fields, models, api


# noinspection PyProtectedMember
class StockPicking(models.Model):
    # Private attributes
    _inherit = "stock.picking"

    # Default methods

    # Fields declaration
    b92_digital_signature = fields.Binary(string='Firma Digital', attachment=True, copy=False)

    # compute and search fields, in the same order of fields declaration

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides
    @api.model
    def create(self, values):
        picking = super(StockPicking, self).create(values)
        if picking.b92_digital_signature:
            values = {'b92_digital_signature': picking.b92_digital_signature}
            picking._track_signature(values, 'b92_digital_signature')
        return picking

    @api.multi
    def write(self, values):
        self._track_signature(values, 'b92_digital_signature')
        return super(StockPicking, self).write(values)

    # Action methods

    # Business methods
