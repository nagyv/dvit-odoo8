{
    'name': 'Invoice Discount',
    'version': '1.0',
    'category': 'Accounting',
    'summary': "Show Discount Total and Total before Discount on Invoices. ",
    'description':"Show Discount Total and Total before Discount on Invoices.",
    'author': 'M.Hagag@DVIT.ME',
    'website': 'http://www.openerp.com',
    'depends': ['account_voucher'],
    'data': [
        'discount_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}


