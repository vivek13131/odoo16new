from odoo import api, fields, models, _

class Students_wizard(models.TransientModel):
    _name = 'library.studentswizard'
    _description = 'its about to change the field value in st.library'

    roll_no = fields.Integer(string="Roll No")
    name = fields.Char(string="Student Name")
    address = fields.Text(string="Address")
    mobile_no = fields.Char(string="Mobile Number")
    course = fields.Selection([
        ('information technology', 'INFORMATION TECHNOLOGY'),
        ('computer Engineering', 'COMPUTER ENGINEERING'),
    ], string=' Course ')
    date_of_birth = fields.Date(string="Dob", )
    age = fields.Integer(string="Age")
    std = fields.Char(string="class")

    #functions

    #update button
    def edit(self):
        # print(self.env.context.get('active_id'))
        for rec in self:
            students = self.env['library.management'].search([('roll_no','=',rec.roll_no)])
            vals = {
                'roll_no': self.roll_no,
                'name': self.name,
                'address': self.address,
                'mobile_no': self.mobile_no,
                'course': self.course,
                'date_of_birth': self.date_of_birth,
                'std': self.std,
            }
            if students:
                students.write(vals)
            else:
                self.env['library.management'].create(vals)


