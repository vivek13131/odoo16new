from odoo import api, fields, models


class Fee_management(models.Model):
    _name = 'library.fee'
    _description = 'fee management'
    name = fields.Char(string="Student name")
    roll_no_ids = fields.Char(string="Roll_no")
    total_fee_ids = fields.Char(string="total_fee")
