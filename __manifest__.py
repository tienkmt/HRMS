# -*- coding: utf-8 -*-
{
    'name': "hrms",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],
    'application': True,
    'sequence': -100,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/hrm_security.xml',
        'views/system_view.xml',
        'views/block_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
