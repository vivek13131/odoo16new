from odoo import api, fields, models


class Staff(models.Model):
    _name = 'library.staff'
    _description = "library staff"
    # _rec_name = 'address'

    staff = fields.Integer(string="Staff ID")
    name = fields.Char(string='Name')
    address = fields.Text(string='Address')
    mobile_no = fields.Integer(string='Mobile Number')
    branch = fields.Selection([
        ('information technology', 'INFOMARTION TECHNOLOGY'),
    ], string='Branch')
    Books_logs_id = fields.Many2many('library.books', string="Book info")

