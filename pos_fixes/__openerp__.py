{
    'name': 'POS Fixes',
    'summary': 'Point of Sale Fixes',
    'description': """
    This module now deppends on IngAdhoc's product_pack.

    https://github.com/ingadhoc/product/tree/8.0/product_pack

    Fixes included:

    - Fix POS invoices payments by reconciling them automatically on POS session closing to get them paid.

    - Complete the anglo-saxon journal entries missing in POS.

    *ToDo*:

        - Handle UoS convertion ex. selling in grams while product UoS is KG .
     """,
    'version': '8.0.2.0',
    'category': 'Point of Sale',
    'author': 'DVIT.me',
    'website': 'http://dvit.me',
    'license': 'AGPL-3',
    'depends': [
        'account_anglo_saxon',
        'account',
        'account_voucher',
        'point_of_sale',
        'product_pack_pos',
    ],
    'data': [],
    'demo': [],
    'installable': True,
    'auto_install': True,
    'application': False,
}
