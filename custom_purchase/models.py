from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many('res.partner', string="Vendors")

class PurchaseOrderBid(models.Model):
    _name = 'purchase.order.bid'
    _description = 'Bids for RFQ'

    order_id = fields.Many2one('purchase.order', string='RFQ Reference', required=True)
    vendor_id = fields.Many2one('res.partner', string='Vendor', required=True)
    bid_amount = fields.Float(string='Bid Amount', required=True)

class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'

    name = fields.Char(string='Request Title', required=True)
    requested_by = fields.Many2one('res.users', string='Requested By', required=True)
    item_ids = fields.One2many('purchase.request.line', 'request_id', string='Items')

class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'Purchase Request Line'

    request_id = fields.Many2one('purchase.request', string='Purchase Request')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True)
