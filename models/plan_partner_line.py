from odoo import _, models, fields, api
from odoo.exceptions import UserError, ValidationError

class PlanPartnerLine(models.Model):
    _name = "plan.partner.line"

    plan_id = fields.Many2one('plan.sale.order', string='Sale Plan', ondelete='cascade')
    partner = fields.Many2one('res.partner', string='Approver')
    status = fields.Selection(string='Status', selection=[
        ('pending', 'Waiting for Approvement'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
    ], required=True, default='pending')

