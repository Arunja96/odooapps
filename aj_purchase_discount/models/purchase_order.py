from odoo import models, fields, api, _
from odoo.tools.misc import formatLang


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    discount = fields.Float(string="Discount (%)")


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    discount_total = fields.Float(string="Discount Total", compute="_compute_dis_totals")

    @api.depends('order_line.discount','order_line.taxes_id')
    def _compute_dis_totals(self):
        if self.order_line:
            discount_prices = []
            for line in self.order_line:
                if line.discount > 0:
                    discount_price = (line.discount / 100) * (line.price_unit * line.product_qty)
                    discount_prices.append(discount_price)
            if discount_prices and self.amount_tax:
                self.discount_total = sum(discount_prices)
                self.amount_total = self.amount_untaxed + self.amount_tax - sum(discount_prices)
            elif discount_prices and not self.amount_tax:
                self.discount_total = sum(discount_prices)
                self.amount_total = self.amount_untaxed - sum(discount_prices)
            else:
                self.discount_total = None
