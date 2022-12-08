from odoo import api, fields, models,_
from odoo.exceptions import UserError


class Library(models.Model):
    _name = 'library.admin'
    _rec_name = "name_id"
    name_id = fields.Many2one('library.management', string="Book Taken list")
    std = fields.Char(string="class", compute="_onchange_name_id")
    course = fields.Char(string="Branch", compute="_onchange_name_id")
    books_items = fields.Many2one('library.books', string="Books Items")
    books_ids = fields.One2many('library.books','item_id',string='Books')



    @api.onchange('books_items')
    def _onchange_author(self):
        for rec in self:
            lines = []
            for book in self.books_items:
                vals = {
                        'name': book.name,
                        'category_id': 1,
                        'book_price': book.book_price,
                    }
                lines.append((0,0,vals))
                rec.books_ids = lines

    @api.onchange('name_id')
    def _onchange_name_id(self):
        if self.name_id:
            if self.name_id.std:
                self.std = self.name_id.std
        else:
            self.std = None
        if self.name_id:
            if self.name_id.course:
                self.course = self.name_id.course
        else:
            self.course = None

    # def write(self, vals):
    #     name = vals['name_id']
    #     if name:
    #         raise UserError(_("The Name is not be editable"))
    #     print(name)
    #     result = super(Library, self).write(vals)
    #     return result
