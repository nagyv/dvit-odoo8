from openerp import api, fields, models

class res_users(models.Model):
	_inherit = 'res.users'
	is_delivery = fields.Boolean(string="Delivery ?")


class pos_order(models.Model):
	_inherit = 'pos.order'
	pos_delivery = fields.Many2one(comodel_name='res.users', string="Delivery Driver", 
		domain=[('is_delivery', '=', True)])

	def _order_fields(self, cr, uid, ui_order, context=None):
		return {
            'name':         ui_order['name'],
            'user_id':      ui_order['user_id'] or False,
            'session_id':   ui_order['pos_session_id'],
            'lines':        ui_order['lines'],
            'pos_reference':ui_order['name'],
            'partner_id':   ui_order['partner_id'] or False,
            "pos_delivery": ui_order['pos_delivery'],
        }