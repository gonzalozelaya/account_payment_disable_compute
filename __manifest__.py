# -*- coding: utf-8 -*-
{
    'name': "Disable compute method for account.payment",

    'summary': """
        This module just disables the compute method for account.payment""",

    'description': """
        This module just disables the compute method for account.payment
    """,

    'author': "OutsourceArg",
    'website': "http://www.outsourcearg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Account',
    'version': '1.0',
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['account','account_payment_pro'],

}