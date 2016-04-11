{
    'name': 'POS anglo-saxon fix',
    'summary': 'create entries to complete anglo-saxon',
    'describtion': """
    complete the anglo-saxon journal entries missing in POS.
    *ToDo*: 
        - Handle UoS convertion ex. selling in grams while product UoS is KG .
     """,
    'version': '8.0.0.1',
    'category': 'Point of Sale',
    'author': 'DVIT.me',
    'website': 'http://dvit.me',
    'license': 'AGPL-3',
    'depends': [
        'account_anglo_saxon',
        'account',
        'point_of_sale',
    ],
    'data': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}