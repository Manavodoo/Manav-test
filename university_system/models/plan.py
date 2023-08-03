from odoo import api,fields, models

class Student(models.Model):
    _name = "university.student"
    _description = "University student"
    name = fields.Char(string='Name')
    age = fields.Integer(string ='Age')
    # gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string = "Gender")



