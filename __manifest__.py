# -*- coding: utf-8 -*-
{
    'name': "Hospital",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Bryan",
    'website': "http://www.yourcompany.com",
    'category': 'Extra Tools',
    'version': '0.1',
    'summary': 'Module for managing the Hospitals',
    'sequence': '10',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/patient.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'instalable': True,
    'application': True,
    'auto_install': False,
}
