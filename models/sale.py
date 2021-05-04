from odoo import _, models, fields, api
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    plan = fields.Many2one('plan.sale.order', string='Sale Plan')

    def _get_plan(self):
        plan = self.env['plan.sale.order'].search([('id', '=', id)], limit=1)
        if plan:
            self.plan = plan

