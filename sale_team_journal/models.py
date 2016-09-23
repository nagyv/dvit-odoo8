

from openerp import models, fields, api


class CRMCaseSection(models.Model):
	_inherit = "crm.case.section"
	journal_id = fields.Many2one('account.journal', 'Sale Journal', domain = [('type', '=', 'sale')], help='Note: when you set a sale journal to a sale user it overwrites this field, the priority is for user and then the team' )

class ResUsers(models.Model):
	_inherit = "res.users"
	journal_id = fields.Many2one('account.journal', 'Sale Journal', domain = [('type', '=', 'sale')])

class SaleOrder(models.Model):
	_inherit = "sale.order"

	def _prepare_invoice(self, cr, uid, order, lines, context=None):
		vals = super(SaleOrder, self)._prepare_invoice(
			cr, uid, order, lines, context=context)
	
		for o in order:
			# get the 1st sale journal by ID instead the default function gets 1st by name
			journal_id = self.pool['account.journal'].search(cr, uid,[
			('type','=','sale'),('company_id','=',order.company_id.id)], 
			limit=1, order='id asc')
			# set the 1st most sale journal by default
			vals['journal_id'] = journal_id[0]
			if o.user_id.journal_id.id:
				vals['journal_id'] = o.user_id.journal_id.id
			elif o.section_id.journal_id.id:
				vals['journal_id'] = o.section_id.journal_id.id
			elif o.user_id.default_section_id.journal_id:
				vals['journal_id'] = o.user_id.default_section_id.journal_id.id
		return vals