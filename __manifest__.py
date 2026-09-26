{
    'name': 'StockSense',
    'version': '1.0.0',
    'category': 'Inventory',
    'summary': 'Modular Inventory Management System (IMS) for real-time stock operations',
    'depends': ['base', 'stock', 'product'],
    'data': [
        'views/dashboard_views.xml',
        'views/product_views.xml',
        'views/operation_views.xml',  # Changed to match your exact file name
        'views/menu.xml',             # Changed to match your exact file name
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}