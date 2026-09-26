{
    'name': 'StockSense',
    'version': '1.0',
    'summary': 'Minimalist, IKEA-inspired Inventory Management System',
    'description': 'A localized, high-contrast inventory tracker with real-time financial metrics and stock health alerts, built for the Odoo x GCET Hackathon.',
    'category': 'Inventory/Inventory',
    'author': 'Your Team Name',
    'depends': ['base', 'stock', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/dashboard_views.xml',
        'views/product_views.xml',
        'views/operation_views.xml',  
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'project-stocksense/static/src/css/ikea.css',
        ],
    },

    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}