from odoo import api, fields, models
from datetime import datetime


class sale_inherit(models.Model):
    _inherit = 'sale.order'
    sale_date = fields.Date(string="Sale Date")
    coust_ids = fields.One2many('customer.inherit', 'user_id', string="Coustomer lines")

    def sale_price(self):
        for rec in self.order_line:
            rec.write({
                'sale_price': 700,
            })


class sale_order_lines_inherit(models.Model):
    _inherit = 'sale.order.line'

    sale_price = fields.Float(string="Sale price")


class customerlines(models.Model):
    _name = 'customer.inherit'
    date = fields.Date(string="Date")
    review = fields.Text(string="Text")
    user_id = fields.Many2one('sale.order')
