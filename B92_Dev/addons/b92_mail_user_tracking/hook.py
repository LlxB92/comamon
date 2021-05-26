from collections import defaultdict

from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})

    # Buscar los mensajes que no sean asociados a adjuntos
    # y  tengan "Nombre de registro del mensaje" vacío
    msgs_rs = env['mail.message'].search(
        [('model', '!=', 'ir.attachment'), ('record_name', '=', False), ('res_id', '!=', False)],
    )

    # Obtener los IDs de cada modelo
    model_id_dct = defaultdict(set)
    for msg in msgs_rs:
        model_id_dct[msg.model].add(msg.res_id)

    # Actualizar el campo "Nombre de registro del mensaje"
    for model in model_id_dct:
        id_record_name_lst = env[model].browse(model_id_dct[model]).exists().name_get()
        for ID, record_name in id_record_name_lst:
            msgs_rs.filtered(lambda m: m.res_id == ID and m.model == model).write({
                'record_name': record_name
            })
