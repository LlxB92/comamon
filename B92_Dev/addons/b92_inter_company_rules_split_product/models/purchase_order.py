# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.exceptions import UserError


# noinspection PyMethodFirstArgAssignment,PyProtectedMember
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def _prepare_sale_order_line_data(self, line, company, sale_id):
        """ Generate the Sales Order Line values from the PO line
            :param line : the origin Purchase Order Line
            :rtype line : purchase.order.line record
            :param company : the company of the created SO
            :rtype company : res.company record
            :param sale_id : the id of the SO
        """
        # Obtener los datos originales
        res = super(PurchaseOrder, self)._prepare_sale_order_line_data(line, company, sale_id)

        # Si el producto es común para todas las compañías, entonces no hacer nada
        if not line.product_id.company_id:
            return res

        # Buscar el producto en la compañía destino
        prod_id = self.env['product.product'].sudo().search([
            ('company_id', '=', company.id), ('default_code', '=', line.product_id.default_code)
        ])

        if prod_id:
            # Calcular los impuestos por defecto a partir del producto buscado.
            # Obtener impuestos por compañía, no por usuario para inter-compañía
            company_taxes = prod_id.taxes_id.filtered(lambda t: t.company_id.id == company.id)
            if sale_id:
                so = self.env["sale.order"].sudo(company.intercompany_user_id).browse(sale_id)
                company_taxes = so.fiscal_position_id.map_tax(company_taxes, prod_id, so.partner_id)

            res['tax_id'] = [(6, 0, company_taxes.ids)]
            res['product_id'] = prod_id.id
            res['product_uom'] = prod_id.uom_po_id.id
        else:
            raise UserError(
                'El producto con referencia interna {} no existe en la compañía {}'.format(
                    line.product_id.default_code, company.name
                )
            )

        return res
