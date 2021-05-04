from odoo import _, models, fields
from odoo.exceptions import UserError, ValidationError

class PlanSaleOrder(models.Model):
    _name = 'plan.sale.order'

    def send_plan(self):
        self.state = 'sent'
        print('Sent')

    name = fields.Text(string='Name', required=True)
    quotation = fields.Many2one('sale.order', string='Quotation', readonly=True, ondelete='cascade')
    detail = fields.Text(string='Detail information about plan', required=True)
    state = fields.Selection([
        ('new', 'New'),
        ('sent', 'Sent'),
        ('approved', 'Approved'),
        ('refuse', 'Refuse'),
    ], string='Status', readonly=True, default='new')
    partner_lines = fields.One2many('plan.partner.line', 'plan_id')

