from openerp import fields, models, api


class sale_order(models.Model):
    _name = "sale.order"
    _inherit = ['sale.order']

    driver_id = fields.Many2one('res.users', 'Driver')
