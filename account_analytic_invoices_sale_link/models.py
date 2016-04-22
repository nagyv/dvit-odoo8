from openerp import models, api
from openerp.osv import osv, fields
class account_analytic_account(osv.osv):
	_inherit = "account.analytic.account"
	_columns = {
	'sale_invoices': fields.boolean('Link recurring invoices to sale order'),
	'auto_confirm_invoices': fields.boolean('Auto confirm generated invoices'),
	}
	# After generating invoice update sale order to include the invoice id

	def _recurring_create_invoice(self, cr, uid, ids, automatic=False, context=None):
		invoice_id = super(account_analytic_account, self)._recurring_create_invoice(cr, 
			uid, ids, False, context=context)[0]
		invoice_obj = self.pool.get('account.invoice').browse(cr, uid, invoice_id, context=context)
		# Get 1st confirmed only Sale order
		for account in self.browse(cr, uid, ids, context=context):
			sale_obj = self.pool.get('sale.order')
			sale_id = sale_obj.search(cr, uid, 
				[('project_id','=', account.id), ('state', '=', 'manual')], context=context)
			if sale_id:
				sale = sale_obj.browse(cr, uid, sale_id, context=context)[0]
				if account.sale_invoices:
					sale.invoice_ids += invoice_obj
				if account.auto_confirm_invoices:
					for inv in sale.invoice_ids:
						inv.state == 'draft' and inv.signal_workflow('invoice_open')
		return invoice_id
