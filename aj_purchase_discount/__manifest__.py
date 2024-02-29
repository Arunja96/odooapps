# -*- coding: utf-8 -*-
{
    'name': 'Purchase Discount',
    'summary': """Discount for purchase""",
    'version': '1.2',
    'author': 'Arun',
    'category': 'Inventory/Purchase',
    'depends': ['purchase'],
    'data': [
        'views/purchase_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'aj_purchase_discount/static/src/components/**/*',
        ],
    },
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
