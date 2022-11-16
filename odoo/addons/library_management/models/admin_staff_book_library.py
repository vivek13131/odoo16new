from odoo import api, fields, models


class staff_recode(models.Model):
    _name = 'libraryadminstaff.book'
    _rec_name = "staff_ids"
    staff_ids = fields.Many2one('library.staff', string="Book Taken staff")
