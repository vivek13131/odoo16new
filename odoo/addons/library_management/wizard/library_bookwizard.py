from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class Libraybooowizard(models.TransientModel):
    _name = 'library.bookwizard'

    isbn = fields.Char(string='isbn')
    name = fields.Char(string='Name')
    author_id = fields.Many2one('library.author', string='Author Name', )
    category_id = fields.Many2one('library.category', string='Category')
    edition = fields.Integer(string='Edition Mark')
    book_price = fields.Float(string='book price')

    def update_d(self):
        for rec in self:
            book = self.env['library.books'].search([('isbn', '=', rec.isbn)])
            vals = {'isbn': self.isbn,
                    'name': self.name,
                    'author_id': self.env.context.get('active_id'),
                    'category_id': self.category_id.id,
                    'edition_mark': self.edition,
                    'book_price': self.book_price,
                    }
            if book:
                book.write(vals)
            else:
                self.env['library.books'].create(vals)



