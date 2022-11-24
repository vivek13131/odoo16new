from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime


class StudentsDetails(models.Model):
    _name = 'library.management'
    _description = "library Students"

    roll_no = fields.Integer(string='Roll Number')
    name = fields.Char(string='Name')
    address = fields.Text(string='Address')
    mobile_no = fields.Char(string='Mobile Number')
    course = fields.Selection([
        ('information technology', 'INFORMATION TECHNOLOGY'),
        ('computer Engineering', 'COMPUTER ENGINEERING'),
    ], string=' Course ')
    product_id = fields.Many2many('library.books', string="product")
    date_of_birth = fields.Date(string="Dob", )
    age = fields.Integer(string="Age")
    std = fields.Char(string="class")

    # book info page
    book_taken = fields.Datetime(string="BOOK TAKEN DATE")
    book_return = fields.Datetime(string="BOOK RETURN DATE")
    fee = fields.Integer(string="FEE for Late ")
    # add_book_ids = fields.One2many('library.books', 'book_name_id', string="Book list")

    @api.model
    def create(self, vals):
        dob = [vals]
        dates = vals['date_of_birth']
        if vals['date_of_birth']:
            if str(dates) >= str(datetime.today().date()):
                raise ValidationError(_('DOB should be less then Today\'s Date.'))
        if not vals['date_of_birth']:
            raise ValidationError(_("please enter your date birth"))
        if 'date_of_birth' not in dob:
            print("The DOB is is exit")
        else:
            print("The Dob is not exit")
        result = super(StudentsDetails, self).create(vals)
        # print(datetime.today())
        return result

    # def write(self, vals):
    #     result = super(StudentsDetails, self).write(vals)
    #     if self.date_of_birth:
    #         if str(self.date_of_birth) >= str(datetime.today().date()):
    #             raise ValidationError(_('DOB should be less than Today\'s Date.'))
    #     if not self.date_of_birth:
    #         raise ValidationError(_("please enter your date birth"))
    #     if not self.date_of_birth:
    #         print(self.date_of_birth)
    #     else:
    #         print("the value not exit")
    #     return result

    def write(self, vals):
        print("1111111", vals)
        dates = vals.get('date_of_birth')
        print("334334", dates)
        if vals.get('date_of_birth'):
            if str(dates) >= str(datetime.today().date()):
                raise ValidationError(_('DOB should be less then Today\'s Date.'))
            else:
                pass
        # else:
        #     raise ValidationError(_("please enter your date birth"))
        result = super(StudentsDetails, self).write(vals)
        return result

    def action_confirm(self):

        dates = self.date_of_birth.year
        print("-----------------------", dates)
        self.age = datetime.today().year - dates
        print(self.age)

