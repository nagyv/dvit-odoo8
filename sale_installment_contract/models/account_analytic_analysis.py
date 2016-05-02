from dateutil.relativedelta import relativedelta
import datetime
import time
from openerp.osv import osv, fields, orm
from openerp import models, api
from openerp.tools.translate import _
from logging import getLogger
from openerp.exceptions import ValidationError

_logger = getLogger(__name__)

class account_analytic_account(osv.osv):
    _inherit = "account.analytic.account"
    _columns = {
        'installment_mode': fields.boolean('Installments mode', help='Link recurring invoices to sale order'),
        'auto_confirm_invoices': fields.boolean('Auto confirm generated invoices'),
    }

    def _recurring_create_invoice(self, cr, uid, ids, automatic=False, context=None):
        invoice_ids = super(account_analytic_account, self)._recurring_create_invoice(cr,
            uid, ids, automatic, context=context)

        # _logger.warning('invoice_ids %s', invoice_ids)

        current_date = time.strftime('%Y-%m-%d')
        if not ids:
            ids = self.search(cr, uid, [
                ('recurring_next_date', '<=', current_date),
                ('state', '=', 'open'), ('recurring_invoices', '=', True),
                ('type', '=', 'contract')])
            # _logger.warning('Account Ids %s', ids)
        for invoice_obj in self.pool.get('account.invoice').browse(cr, uid, invoice_ids, context=context):
            # _logger.warning('invoice Id %s', invoice_obj.id)
            for account in self.browse(cr, uid, ids, context=context):
                # if account:
                #     _logger.warning('Account Id %s', account.id)
                # else:
                #     _logger.warning('Can not find accounts ')
                sale_obj = self.pool.get('sale.order')
                sale_id = sale_obj.search(cr, uid,
                [('project_id', '=', account.id), ('state', '=', 'manual')], context=context)[0]
                # if sale_id:
                #     _logger.warning('Sale Id %s', sale_id)
                # else:
                #     _logger.warning('Sale Id Not found')
                if sale_id:
                    sale = sale_obj.browse(cr, uid, sale_id, context=context)
                    if account.installment_mode:
                        # add invoice_obj only if it's related to contract of sale_obj
                        if invoice_obj.invoice_line[0] and invoice_obj.invoice_line[0].account_analytic_id == sale.project_id:
                            sale.invoice_ids += invoice_obj
                    if account.auto_confirm_invoices:
                        for inv in sale.invoice_ids:
                            inv.state == 'draft' and inv.signal_workflow('invoice_open')
                    if account.recurring_next_date > account.date and account.ca_invoiced == sale.amount_total:
                        account.set_close()
                        sale.signal_workflow('action_invoice_end')
                        sale_obj.write(cr, uid, sale_id, {'state': 'progress'}, context=context)
        return invoice_ids
