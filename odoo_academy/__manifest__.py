# -*- coding: utf-8 -*-
    
{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage training""",
    
    'descrption': """
        Academy module to manage Training: 
        - Courses
        - Sessions
        - Attendances
    """,
    
    'Author': 'Sven',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
    ],
    
    'demo': [
        'demo/academy_demo.xml',        
    ],
}