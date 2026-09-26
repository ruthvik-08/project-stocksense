from odoo import models, fields, api

class ProductTemplateCustom(models.Model):
    _inherit = 'product.template'

    # Custom field to define what "Low Stock" means for this specific product
    low_stock_threshold = fields.Float(string="Low Stock Threshold", default=10.0)
    
    # Computed field to power the Dashboard KPI dynamic filters
    is_low_stock = fields.Boolean(
        string="Is Low Stock",
        compute="_compute_is_low_stock",
        store=True,
        help="Check if current stock is below the threshold for Dashboard Alerts"
    )

    @api.depends('qty_available', 'low_stock_threshold')
    def _compute_is_low_stock(self):
        for record in self:
            if record.type == 'product': # Only track storable products
                record.is_low_stock = record.qty_available <= record.low_stock_threshold
            else:
                record.is_low_stock = False