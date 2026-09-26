from odoo import models, fields, api

class ProductTemplateCustom(models.Model):
    _inherit = 'product.template'

    low_stock_threshold = fields.Float(string="Low Stock Threshold", default=10.0)
    
    is_low_stock = fields.Boolean(
        string="Is Low Stock",
        compute="_compute_is_low_stock",
        store=True
    )

    @api.depends('qty_available', 'low_stock_threshold')
    def _compute_is_low_stock(self):
        for record in self:
            if record.type == 'product': 
                record.is_low_stock = record.qty_available <= record.low_stock_threshold
            else:
                record.is_low_stock = False