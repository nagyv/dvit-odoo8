# -*- coding: utf-8 -*-
from openerp import http

# class InvoiceView(http.Controller):
#     @http.route('/invoice_view/invoice_view/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_view/invoice_view/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_view.listing', {
#             'root': '/invoice_view/invoice_view',
#             'objects': http.request.env['invoice_view.invoice_view'].search([]),
#         })

#     @http.route('/invoice_view/invoice_view/objects/<model("invoice_view.invoice_view"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_view.object', {
#             'object': obj
#         })