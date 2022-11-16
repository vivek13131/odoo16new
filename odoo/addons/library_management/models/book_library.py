from odoo import api, fields, models,_
from odoo .exceptions import ValidationError
from datetime import datetime

class BooksDeatil(models.Model):
    _name = 'library.books'
    _description = "library books"
    isbn = fields.Char(string="ISBN_no")
    # book_name_id = fields.Many2one('library.management', string="book_number")
    author_id = fields.Many2one('library.author', string="Author", )
    book_reference = fields.Text(string="Book Reference")
    name = fields.Char(string="Name")
    edition_mark = fields.Char(string="Edition Mark")
    date_of_publication = fields.Date(string="Date of Publication")
    volume_number = fields.Integer(string="Volume_numbers")
    publication = fields.Char(string="Publication")
    category_id = fields.Many2one('library.category', string="Category")
    img = fields.Binary(string="image")
    status = fields.Boolean(string="Available")
    book_price = fields.Float(string="Price")

    # student_id = fields.Many2one('library.management',string="Studentname")
    # The author id is connect to one2many moudle author.library
    @api.model
    def create(self, vals):
        # if 'company_id' in vals:
        #     self = self.with_company(vals['company_id'])
        # if vals.get('name', _('New')) == _('New'):
        #     seq_date = None
        #     if 'date_order' in vals:
        #         seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
        #     vals['name'] = self.env['ir.sequence'].next_by_code('sale.order', sequence_date=seq_date) or _('New')
        result = super(BooksDeatil, self).create(vals)
        # print("hello",self,vals)
        return result

    # def write(self, values):
    #     print(self)
    #     result = super(BooksDeatil, self).write(values)
    #     # print(result)
    #     return result

    def unlink(self):
        # print(self)
        result = super(BooksDeatil, self).unlink()
        print(result)
        return result

    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            book = self.env['library.books'].search([('name','=',rec.name),('id','!=',rec.id)])
            if book:
                raise ValidationError(_(" the book name is already enter"))

    @api.constrains('date_of_publication')
    def _check_date_of_publication(self):
        if self.date_of_publication > fields.Date.today():
            raise ValidationError(_("The publication date is wrong"))
