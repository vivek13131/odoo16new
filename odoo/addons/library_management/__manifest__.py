{
    'name': 'library management',
    'version': '1.0.0',
    'category': 'library/library',
    'summary': 'the module contain the library systems',
    'description': """
    This module contains all the common features of library management""",
    'depends': ['base'],
    'data': [
    	'security/ir.model.access.csv',
        'views/library_admin_views.xml',
        'views/library_staff_views.xml',
        'views/library_students_views.xml',
        'views/library_book_views.xml',
        'views/library_author_views.xml',
        'views/library_category_views.xml',
        'views/library_fee_views.xml',
        'views/library_admin_staff_book_views.xml',
        
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',

}