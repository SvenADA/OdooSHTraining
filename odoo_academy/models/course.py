# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Informacion del curso'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    
    level = fields.Selection(string='Level',
                            selection=[('principiante', 'Principiante'),
                                      ('intermedio', 'Intermedio'),
                                      ('avanzado', 'Avanzado')],
                            copy=False)
    active = fields.Boolean(string='Activo', default=True)