{
    'name': 'Invoice Amount in Words',
    'summary': """Total Amount in Word for Invoicing both in view
    and report.""",
    'version': '1.1',
    'category': 'Accounting/Accounting',
    'author': 'Arun',
    'depends': ['account'],
    'data': [
        'views/account_view.xml',
        'report/report.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}
