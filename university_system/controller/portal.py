from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
from odoo import http
import logging
logger = logging.getLogger(__name__)

class StudentPortal(CustomerPortal):


    @http.route('/students', website =True, auth ='user')
    def students(self, **kwargs):
        students = http.request.env['university.student'].sudo().search([])
        logger.debug(students)
        print(students)

        return http.request.render("university_system.detail", {'student_data': students})

    def _prepare_home_portal_values(self,counters):
        rtn = super(StudentPortal,self)._prepare_home_portal_values(counters)
        rtn['student_counts'] = request.env['university.student'].search_count([])
        return rtn


    @http.route(['/my/students'],website =True, auth ='user')
    def listView(self, **kw):
        print("Hello")    
        students = http.request.env['university.student'].sudo().search([])
        vals = {'students': students ,'page_name' :'students_list_view'}
        return http.request.render("university_system.student_list_view", vals)
    

    @http.route('/my/update_student/<int:student_id>', website=True, auth='user')
    def update_student(self, student_id, **kwargs):
        student = http.request.env['university.student'].sudo().browse(student_id)
        return http.request.render("university_system.custom_student_form_view", {'student': student})


    @http.route('/my/do_update_student', type='http', auth='user', methods=['POST'], website=True)
    def do_update_student(self, **post):
        student_id = int(post.get('student_id'))
        student = http.request.env['university.student'].sudo().browse(student_id)
        print(student)
        print(post.get('name'))
        print(post.get('age'))
        student.write({
            'name': post.get('name'),
            'age': int(post.get('age'))
        })
        return http.request.redirect('/my/students')
    
    

