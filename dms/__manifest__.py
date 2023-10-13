# -*- coding: utf-8 -*-


{
    'name': 'dms',
    'version': '1',
    'sequence': -100,
    'summary': 'doctor Management Application for odoo ',
    'description': """ .""",
    'author': 'alaa samy',
    'company': 'alaasamy',
    'maintainer': ' ',
    'category': 'Sales',
    'website': 'www.alaa.com',
    'depends': ['base',],
    'data': [

        'reports/patients_templet.xml',
        'reports/patients_action_report.xml',


        'views/doctor.xml',
        'views/patients.xml',
        'views/specialization.xml',
        'views/slots.xml',
        'views/appointment.xml',
        'views/medical.xml',

        'views/menus.xml',


    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
