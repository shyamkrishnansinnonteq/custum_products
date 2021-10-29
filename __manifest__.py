{
    'name': 'Custum products',
    'summary': """Custum products""",
    'version': '1.0.0.0.0',
    'description': """Custum products""",
    'author': 'Shyam',
    'company': 'Sinnonteq',
    'website': 'https://www.sinnonteq.com',
    'category': 'Extra Tools',
    'depends': [
        'sale',
        'account',
        'field_force',
        'product',
        'mail',
    ],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/product.xml',
        'views/sale.xml',
	],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}


