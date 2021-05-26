# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.exceptions import UserError


# noinspection PyMethodFirstArgAssignment,PyProtectedMember
class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def _prepare_purchase_order_line_data(self, so_line, date_order, purchase_id, company):
        """ Generate purchase order line values, from the SO line
            :param so_line : origin SO line
            :rtype so_line : sale.order.line record
            :param date_order : the date of the orgin SO
            :param purchase_id : the id of the purchase order
            :param company : the company in which the PO line will be created
            :rtype company : res.company record
        """
        # Obtener los datos originales
        res = super(SaleOrder, self)._prepare_purchase_order_line_data(so_line, date_order, purchase_id, company)

        # Si el producto es común para todas las compañías, entonces no hacer nada
        if not so_line.product_id.company_id:
            return res

        # Buscar el producto en la compañía destino
        prod_id = self.env['product.product'].sudo().search([
            ('company_id', '=', company.id), ('default_code', '=', so_line.product_id.default_code)
        ])

        if prod_id:
            # Calcular los impuestos por defecto a partir del producto buscado.
            # Obtener impuestos por compañía, no por usuario para inter-compañía
            company_taxes = prod_id.supplier_taxes_id.filtered(lambda t: t.company_id == company)
            if purchase_id:
                po = self.env["purchase.order"].sudo(company.intercompany_user_id).browse(purchase_id)
                company_taxes = po.fiscal_position_id.map_tax(company_taxes, prod_id, po.partner_id)

            res['taxes_id'] = [(6, 0, company_taxes.ids)]
            res['product_id'] = prod_id.id
            res['product_uom'] = prod_id.uom_po_id.id
        else:
            raise UserError(
                'El producto con referencia interna {} no existe en la compañía {}'.format(
                    so_line.product_id.default_code, company.name
                )
            )

        return res
