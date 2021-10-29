from odoo import models, fields


class custumProductProduct(models.Model): 
    _name = "custumizeproduct.product"
    # _inherit = 'mail.thread'
    _inherits = {'product.product': 'custumizeproduct_product_id'}
    # _inherit = 'product.product'
    

    custumizeproduct_product_id =  fields.Many2one('product.product', String='Product')
    # cust_product_tmpl_id =  fields.Many2one('mail.thread', String='Product department')
    test3 = fields.Text(String='Test4')

    
# class custumProductProduct(models.Model): 
#     _name = "custumproduct.product"
#     _inherits = {'': 'cust_product_tmpl_id'} 

#     cust_product_tmpl_id =  fields.Many2one('product.product', String='Product ', required=True)
#     test3 = fields.Text(String='Test3')

# custumProductProduct()