import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta
from operator import itemgetter
import time

import openerp
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.osv import fields, osv, expression
from openerp.tools.translate import _
from openerp.tools.float_utils import float_round as round
from openerp.tools.safe_eval import safe_eval as eval

import openerp.addons.decimal_precision as dp

class account_account(osv.osv):
    _inherit = "account.account"
    _columns = {
        'name': fields.char('Name', required=True, select=True, translate=True,),
        }
    
class account_journal(osv.osv):
    _inherit = "account.journal"
    _columns = {
        'name': fields.char('Journal Name', required=True, translate=True,),
        }
    
