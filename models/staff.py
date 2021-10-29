from odoo import models, fields

# class MyAccountInvoice(models.Model):
#     _name = 'custom.partner'
#     _inherits = {'account.invoice': 'custum_partner_id'}
#     _description = 'custom partner'

#     test1 = fields.Text(String='Test1')
#     custum_partner_id = fields.Many2one('account.invoice')
    
# MyAccountInvoice()



# class CustumFieldStaff(models.Model): 
#     _name = "custumfieldforce.staff"
#     _inherits = {'field_force.field_staff': 'cust_staff_id'} 

#     cust_staff_id =  fields.Many2one('field_force.field_staff', String='staff')
#     test2 = fields.Text(String='Test2')

class CustumFieldStaff(models.Model): 
    _name = "custumfieldforce.staff"
    _inherit = 'field_force.field_staff'

    cust_staff_id =  fields.Many2one('field_force.field_staff', String='staff')
    test2 = fields.Text(String='Test2')

CustumFieldStaff()