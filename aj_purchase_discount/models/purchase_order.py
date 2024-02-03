from odoo import models, fields, api, _
from odoo.tools.misc import formatLang


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    discount = fields.Float(string="Discount (%)")

    # discount = fields.Float(
    #     string="Discount (%)",
    #     compute='_compute_discount',
    #     digits='Discount',
    #     store=True, readonly=False, precompute=True)

    @api.onchange('discount')
    def onchange_purchase_discount(self):
        for rec in self:
            if rec.discount > 0:
                discount_price = (rec.discount / 100) * (rec.price_unit * rec.product_qty)
                rec.price_subtotal = rec.price_subtotal - discount_price


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def _compute_tax_totals(self):
        res = super(PurchaseOrder, self)._compute_tax_totals()
        if self.order_line:
            discount_prices = []
            for line in self.order_line:
                if line.discount > 0:
                    discount_price = (line.discount / 100) * (line.price_unit * line.product_qty)
                    discount_prices.append(discount_price)
            self.tax_totals['discount_prices'] = formatLang(self.env, sum(discount_prices),
                                                            currency_obj=line.currency_id or line.company_id.currency_id)
            discount_total = self.tax_totals['amount_total'] - sum(discount_prices)
            self.tax_totals['discount_total'] = formatLang(self.env, discount_total,
                                                           currency_obj=line.currency_id or line.company_id.currency_id)
            print()
        return res
