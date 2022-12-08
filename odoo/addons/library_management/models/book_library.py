from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
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
    item_id = fields.Many2one('library.admin', string="Items")
    ref_no = fields.Char(string="squence")


    # student_id = fields.Many2one('library.management',string="Studentname")
    # The author id is connect to one2many moudle author.library
    @api.model
    def create(self, vals):
        if vals.get('ref_no', _('New')) == _('New'):
            vals['ref_no'] = self.env['ir.sequence'].next_by_code('library.books') or _('New')
        print(vals['ref_no'])
        result = super(BooksDeatil, self).create(vals)
        #     print(result)
        return result

    def unlink(self):
        # print(self)
        result = super(BooksDeatil, self).unlink()
        print(result)
        return result

    # @api.constrains('name')
    # def _check_name(self):
    #     for rec in self:
    #         book = self.env['library.books'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
    #         if book:
    #             raise ValidationError(_(" the book name is already enter"))

    @api.constrains('date_of_publication')
    def _check_date_of_publication(self):
        if self.date_of_publication:
            if self.date_of_publication > fields.Date.today():
                raise ValidationError(_("The publication date is wrong"))

    def books(self):
        books = self.mapped('author_id')
        action = self.env['ir.actions.actions']._for_xml_id('library_management.action_library_book')

        if len(books) > 1:
            action['domain'] = [('id', 'in', books.ids)]
            print(action['domain'])
        elif len(books) == 1:
            form_view = [(self.env.ref('library_management.view_library_book_form').id, 'form')]
            print(form_view)
            if 'views' in action:
                action['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
                action['res_id'] = books.id
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action
