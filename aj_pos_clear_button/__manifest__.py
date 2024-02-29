# -*- coding: utf-8 -*-
{
    'name': 'POS Clear Orderline',
    'summary': """Clear all order lines in one click or one by one""",
    'version': '1.2',
    'author': 'Arun',
    'category': 'Sales/Point of Sale',
    'depends': ['point_of_sale'],
    'data': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        'point_of_sale.assets': [
            "aj_pos_clear_button/static/src/js/clear_button.js",
            "aj_pos_clear_button/static/src/xml/clear_button.xml",
            "aj_pos_clear_button/static/src/js/clearitem_icon.js",
            "aj_pos_clear_button/static/src/xml/clear_item_buttom.xml",
        ]
    },
    'images': ['static/description/banner.gif'],
}
