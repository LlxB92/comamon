# -*- coding: utf-8 -*-

from odoo import api, models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.multi
    def button_cancel(self):
        if not self.user_has_groups('blm92_cancel_account_move.group_cancel_account_move'):
            raise UserError(_(
                # 'You cannot modify a posted entry of this journal.\n'
                # 'First you must be a member of "Allow journal related invoice or entry cancellations" role'
                'No puede modificar un asiento publicado de este diario.\n'
                'Antes tendrá que ser miembro del rol '
                '"Permitir cancelación de asientos contables o facturas en los diarios"'
            ))

        return super().button_cancel()
