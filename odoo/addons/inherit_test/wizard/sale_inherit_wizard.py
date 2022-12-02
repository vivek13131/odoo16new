from odoo import api, models, fields, _
from datetime import datetime
from odoo.exceptions import ValidationError


class sale_wizard(models.TransientModel):
    _name = 'sale.inheritwizard'

    date = fields.Date(string="Date", )  # default=datetime.today()
    text = fields.Text(string="Text")
    coust_ids = fields.One2many('customer.inherit', 'user_id', string="Coustomer lines")

    def update(self):
        print(self.env.context.get('active_id'))
        vals = {
            'date': self.date,
            'review': self.text,
            'user_id': self.env.context.get('active_id'),
        }
        self.env['customer.inherit'].create(vals)
        last = self.env['sale.order'].browse(self.env.context.get('active_id'))
        last.action_confirm()

    @api.model
    def default_get(self, fields):
        res = super(sale_wizard, self).default_get(fields)
        res.update(
            date=datetime.today()
        )
        return res
