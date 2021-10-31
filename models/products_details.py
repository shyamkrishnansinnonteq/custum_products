from odoo import models, fields
class ProductDetailsRecords(models.Model):
    _name = "custum_products.products_details"
    _description = 'product addition'

    name = fields.Char(string='Product Name', required=True)
    photo = fields.Binary(string='Product Photo')
    stock = fields.Integer(string='Number of Stock', required=True)
    color = fields.Selection([
        ('other', 'Regular color'),
        ('Yellow', 'Yellow'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ], required=True, default='other')
    

    