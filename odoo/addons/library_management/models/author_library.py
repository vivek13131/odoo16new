from odoo import api, fields, models


class author(models.Model):
    _name = 'library.author'
    _description = 'author library'

    name = fields.Char(string="Authorname")
    date_of_birth = fields.Date(string="DOB")
    awards = fields.Text(string="Awards")
    biography = fields.Text(string="Biography")
    image = fields.Binary(string="Image")
    total_amount = fields.Char(string="total", compute='_compute_total', store=True)
    # Books_ids = fields.Many2many('library.books', 'author_book_rel', 'author_id' 'book_id', string="Books")
    book_log_ids = fields.One2many('library.books', 'author_id', string="Book log")
    reg_no = fields.Char(string="Reg_no:")
    phone = fields.Integer(string="Phone_no")
    res_user = fields.Many2one('res.users', string="related user")

    def total_action(self):
        total = 0
        for rec in self.book_log_ids:
            if rec:
                val = rec.book_price
                total += val
        self.total_amount = total

    def add_Book(self):
        vals = {
            'isbn': 87898,
            'name': 'self',
            'author_id': self.id,
            'category_id': 1,
            'edition_mark': 1,
            'volume_number': 2,
            'book_price': 400,
        }
        self.env['library.books'].create(vals)

    def total_search(self):
        total = 0.0
        amount = self.env['library.books'].search([('author_id', '=', self.id)])
        for rec in amount:
            if rec:
                val = rec.book_price
                total += val
        self.total_amount = total

    @api.depends('book_log_ids.book_price')
    def _compute_total(self):
        total = 0
        for rec in self.book_log_ids:
            if rec:
                val = rec.book_price
                total += val
        self.total_amount = total

    # sql contraints to check the  name are unique
    _sql_constraints = [
        ('unique_name_', 'unique (name)', 'The author is already entered !')
    ]

    def create_books(self):
        books = self.mapped('book_log_ids')
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
