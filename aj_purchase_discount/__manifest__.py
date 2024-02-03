{
    'name': 'Purchase Discount',
    'version': '16.0.1.0.0',
    'summary': 'Discount fields for purchase',
    'category': 'Inventory/Purchase',
    'author': 'Arun',
    'depends': ['purchase', 'account'],
    'data': [
        'views/purchase_order_view.xml',
    ],
    'images': ['static/description/icon.png'],
    'assets': {

        'web.assets_backend': [
            'aj_purchase_discount/static/src/components/**/*',
        ]},
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
