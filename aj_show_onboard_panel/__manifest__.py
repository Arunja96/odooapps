{
    'name': 'Show Onboarding Panel',
    'version': '16.0.1.0.0',
    'summary': 'Easily close or open onboarding in sales, accounting etc.',
    'description': """
    Show the closed onboarding panel in sales, account. go to companies in setting select not done on onboarding
     panel Tab.""",
    'depends': ['sale', 'account',],
    'data': [
        'views/res_company.xml',
    ],
    'category': 'Uncategorized',
    'author': 'Arun',
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
