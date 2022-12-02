{
    'name': 'inherit',
    'version': '1.0.0',
    'category': 'inherit/inherit',
    'summary': 'the module contain inherit',
    'description': """
    To test the inherit m""",
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_inherit_wizard.xml',
        'views/sale_inherit.xml',
        'views/sale_order_line_inherit.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',

}
