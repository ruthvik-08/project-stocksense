{
    'name': 'StockSense',
    'version': '1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Modular Inventory Management System (IMS) for real-time stock operations',
    'description': """
        StockSense: Centralized Inventory Management System
        ===================================================
        Digitizes and streamlines warehouse operations, replacing manual registers and Excel sheets.
        
        Core Features:
        * Dynamic Dashboard KPIs (Total Products, Low Stock, Pending Receipts/Deliveries)
        * Product Management (SKU, Category, UoM, Reordering Rules)
        * Operations: Receipts (Incoming), Delivery Orders (Outgoing), Internal Transfers
        * Stock Adjustments & Movement History
        * Multi-warehouse support and low stock alerts
    """,
    'author': 'Your Name/Team',
    'website': 'https://github.com/yourusername/stocksense',
    'license': 'LGPL-3',
    'depends': [
        'base', 
        'mail',      # For notifications and OTP password resets
        'product',   # For core product management
        'stock'      # Odoo's core inventory module to build upon
    ],
    'data': [
        # Security rules and access rights
        'security/security.xml',
        'security/ir.model.access.csv',
        
        # Views and UI components
        'views/dashboard_views.xml',
        'views/product_views.xml',
        'views/receipt_delivery_views.xml',
        'views/internal_transfer_views.xml',
        'views/stock_adjustment_views.xml',
        
        # Menus (must be loaded last to reference above actions)
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # Add custom CSS/JS for your dashboard UI here
            # 'stocksense/static/src/css/dashboard.css',
            # 'stocksense/static/src/js/dashboard.js',
        ],
    },
    'installable': True,
    'application': True, # Set to True so it shows up in the main app list
    'auto_install': False,
}