{
    'name': 'Account Analytic Sale Invoices',
    'summary': 'Link recurring invoices to sale order',
    'describtion': """Link the generated recurring invoices to the sale order of the analytic account.
    This is mostly useful if we need to reconcile the generated invoices with a confirmed sale order.
    A generic use case is installments on sale order.
     """,
    'version': '8.0.0.2',
    'category': 'Accounting',
    'author': 'DVIT.me',
    'website': 'http://dvit.me',
    'license': 'AGPL-3',
    'depends': [
        'account_analytic_analysis',
        'account',
        'sale',
    ],
    'data': ['views.xml'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}