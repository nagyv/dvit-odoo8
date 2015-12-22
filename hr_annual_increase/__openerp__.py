# -*- coding: utf-8 -*-
{
    'name': "Annual Salary Increase",

    'summary': """
                 Annual Salary Increase """,

    'description': """
        Increasing The salary by basic percentage every year
    """,
    'author': "Dvit",
    'website': "http://www.Dvit.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'test',
    'version': '3.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_contract','hr_payroll','hr_payroll_account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'hr_payroll.xml'
    ],

}