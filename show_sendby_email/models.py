# -*- coding: utf-8 -*-

from openerp import models, fields, api

class invoice_view(models.Model):
      _name = "ivoice.view"
      _inherit = 'account.invoice'

