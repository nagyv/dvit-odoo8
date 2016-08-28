{
    'name': 'POS payment no barcode',
    'summary': 'POS payment no barcode',
    'description': """
POS payment no barcode
========================
Disallow payments greater than order amount * 100 on POS to handle barcode reading on payment screen.
""",
    'version': '8.0.1.0',
    'category': 'Point of Sale',
    'author': 'DVIT.me',
    'website': 'http://dvit.me',
    'license': 'AGPL-3',
    'depends': [
        'point_of_sale',
    ],
    'data': ['views.xml'],
    'demo': [],
    'installable': True,
    'auto_install': True,
    'application': False,
}