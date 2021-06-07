import json

from odoo import api, fields, models


# noinspection PyProtectedMember
class IrAttachmentBulkModification(models.TransientModel):
    # Private attributes
    _name = 'b92.documents.bulk.modification'
    _description = 'Permite modificar los campos de múltiples archivos a la vez'

    # Fields declaration
    b92_folder_id = fields.Many2one('documents.folder', string='Carpeta')
    b92_tag_ids = fields.Many2many(
        'documents.tag', string="Etiquetas", relation='b92_attachment_doc_tag_rel',
        column1='attachment_id', column2='tag_id',
    )
    b92_owner_id = fields.Many2one('res.users', string="Propietario")
    b92_partner_id = fields.Many2one('res.partner', string="Contacto")
    b92_res_model = fields.Char(string='Modelo del recurso')
    b92_res_id = fields.Integer(string='ID del recurso')

    b92_del_folder = fields.Boolean(string='Quitar carpeta')
    b92_del_tags = fields.Boolean(string='Quitar etiquetas')
    b92_del_owner = fields.Boolean(string='Quitar propietario')
    b92_del_partner = fields.Boolean(string='Quitar contacto')

    b92_tag_count = fields.Integer(string='Cantidad de Etiquetas', compute='_compute_b92_tag_count')

    # compute and search fields, in the same order of fields declaration
    @api.multi
    @api.depends('b92_tag_ids')
    def _compute_b92_tag_count(self):
        for rec in self:
            rec.b92_tag_count = len(rec.b92_tag_ids)

    # Constraints and onchanges

    # CRUD methods (and name_get, name_search, ...) overrides

    # Action methods
    @api.multi
    def action_bulk_modification(self):
        self.ensure_one()
        active_ids = self.env.context.get('active_ids')

        return (
            self._show_mod_rec_view(active_ids)
            if self._modify_attachments(self._convert2write(self), active_ids)
            else dict()
        )

    # Business methods
    @api.model
    def _convert2write(self, rec):
        write_dct = {
            name: rec._fields[b92_name].convert_to_write(rec[b92_name], rec)
            for b92_name, name in self._field_tpl()
            if rec[b92_name]
        }

        write_dct.update(self._del_field_dct(rec))

        return write_dct

    @api.model
    def _del_field_dct(self, rec):
        del_field_tpl = self._del_field_tpl()
        return {
            name: val
            for del_name, name, val in del_field_tpl
            if rec[del_name]
        }

    @api.model
    def _field_tpl(self):
        return [
            ('b92_folder_id', 'folder_id'), ('b92_tag_ids', 'tag_ids'), ('b92_res_model', 'res_model'),
            ('b92_owner_id', 'owner_id'), ('b92_partner_id', 'partner_id'), ('b92_res_id', 'res_id'),
        ]

    @api.model
    def _del_field_tpl(self):
        return [
            ('b92_del_folder', 'folder_id', False), ('b92_del_tags', 'tag_ids', (5, 0, 0)),
            ('b92_del_owner', 'owner_id', False), ('b92_del_partner', 'partner_id', False)
        ]

    @api.model
    def _modify_attachments(self, val_dct, active_ids):
        return self.env['ir.attachment'].browse(active_ids).write(val_dct) if val_dct else False

    @api.model
    def _show_mod_rec_view(self, active_ids):
        # Mostrar vista lista con los adjuntos modificados
        doc_debug_action_dct = self.env.ref('documents.document_debug_action').read()[0]
        doc_debug_action_dct.update({
            'name': 'Adjuntos Modificados',
            'domain': json.dumps([
                ('id', 'in', active_ids),
            ])
        })

        return doc_debug_action_dct
