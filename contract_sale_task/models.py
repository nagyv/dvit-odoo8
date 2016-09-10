# -*- coding: utf-8 -*-

from openerp import models, fields, api



class saleOrder(models.Model):
	_inherit = 'sale.order'

	client_order_ref = fields.Char(string="Reference/Description", required=True)
	def action_button_confirm(self, cr, uid, ids, context=None):
		old_action_button_confirm = super(saleOrder, self).action_button_confirm(cr, uid, ids, context)
		project_task_obj = self.pool.get('project.task')
		sale_order = self.browse(cr, uid, ids[0])
		order_lines_for = sale_order.order_line
		for order in order_lines_for:
			task_id = project_task_obj.search(cr, uid, [('sale_line_id','=', order.id)])
			task_record = project_task_obj.browse(cr, uid, task_id)
			task_record[0].name = task_record[0].name + " " + "[" + sale_order.client_order_ref + "]"
		return old_action_button_confirm

