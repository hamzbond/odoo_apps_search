{
    'name': 'Odoo Apps Search Enhancements',
    'version': '16.0.1.0.0',
    'summary': 'Enhancements for searching and filtering apps in Odoo',
    'description': """
        This module adds the following features to the Odoo Apps menu:
        - Search by author and website
        - Filter by demo data
        - Group by author, website, category, and license
    """,
    'author': 'Hamzbond',
    'website': 'https://hamzbond.github.io',
    'support': 'hamzbond@gmail.com',
    'category': 'Tools',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/app_search_views.xml',
    ],
    'installable': True,
    'application': False,
}