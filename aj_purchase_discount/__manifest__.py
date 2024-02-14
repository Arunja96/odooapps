{
    'name': 'Purchase Discount',
    'version': '12.0.1.0.0',
    'summary': 'Discount fields for purchase',
    'description': """
    Add a discount for purchase line item """,
    'category': 'Inventory/Purchase',
    'author': 'Arun',
    'depends': ['purchase', 'account'],
    'data': [
        'views/purchase_order_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
