from odoo import models, fields, api, _
from odoo.tools.misc import formatLang
from odoo.tools.misc import formatLang


class Purchase(models.Model):
    _inherit = 'purchase.order'

    discount_total = fields.Float(string="Total Discount", compute="_compute_discount_total")

    @api.depends('order_line.discount_price')
    def _compute_discount_total(self):
        for rec in self:
            if rec.order_line:
                discount_amount = sum(rec.order_line.mapped('discount_price'))
                rec.discount_total = discount_amount

    @api.depends('discount_total')
    def _compute_tax_totals(self):
        res = super(Purchase, self)._compute_tax_totals()
        for rec in self:
            total = (rec.amount_untaxed + rec.amount_tax) - rec.discount_total
            rec.tax_totals.update({
                'model': 'purchase.order',
                'formatted_discount_amount': formatLang(self.env, rec.discount_total,
                                                        currency_obj=rec.currency_id),
                'formatted_amount_total_with_discount': formatLang(self.env, total,
                                                                   currency_obj=rec.currency_id),
            })
        else:
            rec.tax_totals['formatted_amount_total_with_discount'] = formatLang(self.env, rec.amount_total,
                                                                                currency_obj=rec.currency_id)
        return res

    def _amount_all(self):
        res = super()._amount_all()
        for order in self:
            if order.discount_total:
                order.amount_total = (order.amount_untaxed + order.amount_tax) - order.discount_total
        return res


class PurchaseLine(models.Model):
    _inherit = 'purchase.order.line'

    discount = fields.Float(string="Discount (%)")
    discount_price = fields.Float(string="Discount Price", compute="compute_discount_price")

    @api.depends('discount')
    def compute_discount_price(self):
        for rec in self:
            if rec.discount > 0:
                price = (rec.discount / 100) * rec.price_subtotal
                rec.discount_price = price
            else:
                rec.discount_price = None

    @api.depends('discount')
    def _compute_amount(self):
        res = super()._compute_amount()
        return res
