# -*- coding: utf-8 -*-
from odoo import models,fields

class habitacion(models.Model):
    _name = 'motel.habitaciones'

    habitaciones = fields.Char(string='Habitaciones')
    nivel = fields.Selection([('1'),('2')],string='Nivel')
    


    _sql_constraints = [
        ('unique_habitacion', 'unique (name)', 'la habitacion ya existe!')
    ]
