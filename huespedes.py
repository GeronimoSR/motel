# -*- coding: utf-8 -*-
from dataclasses import field
from odoo import models,fields

class huespedes(models.Model):
    _name = 'motel.huespedes'

    name = fields.Char(string='NumCliente')
    nombre = fields.Char(string='Nombre y Apellidos')
    telefono = fields.Char(string='Teléfono')
    sexo = fields.Selection([('f','Femenino'),('m','Masculino')],string='Sexo')
    edad = fields.Integer(string='Edad')
    reservacion = fields.Boolean(string='Reservacion')
    habitacion =fields.integer(string='Habitacion')

    
