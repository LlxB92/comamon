# -*- coding: utf-8 -*-

from odoo import fields, models


class CrmPhonecall2phonecall(models.TransientModel):
    """Added the details of the crm phonecall2phonecall."""

    _inherit = 'crm.phonecall2phonecall'
    _description = 'Phonecall To Phonecall'

    tag_ids = fields.Many2many(
        relation='crm_phonecall2phonecall_tag_rel',
    )
