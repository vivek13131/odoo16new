from odoo import api, fields, models


class Category(models.Model):
    _name = 'library.category'
    _description = 'category details'

    name = fields.Char(string="Category")
    books_list_ids = fields.One2many('library.books', 'category_id', string="Book list")

#
