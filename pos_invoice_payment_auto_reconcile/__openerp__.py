{
    'name': 'POS Invoices payments reconcile',
    'summary': 'Auto Reconcile POS invoices payments',
    'version': '8.0.0.1',
    'category': 'Point of Sale',
    'description': """
    Installing this module will fix POS invoices payments by reconciling them automatically on pos session closing.
    this module is fully based on GRAP module pos_invoicing 
    """,
    'author': 'DVIT.me, GRAP',
    'website': 'http://dvit.me',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'account_voucher',
        'point_of_sale',
    ],
    'data': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}