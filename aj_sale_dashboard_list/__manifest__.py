{
    'name': 'Sale Dashboard in List View',
    'version': '16.0.1.0.0',
    'summary': 'Dashboard in sale view',
    'category': 'Sales/Sales',
    'author': 'Arun',
    'website':'https://github.com/Arunja96/odooapps/tree/16.0',
    'depends': ['sale'],
    'data': [
        'views/sale_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'aj_sale_dashboard_list/static/src/views/*.js',
            'aj_sale_dashboard_list/static/src/**/*.xml',
        ],
    },
    'license': 'LGPL-3',
}
