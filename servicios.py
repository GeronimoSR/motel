# -*- coding: utf-8 -*-
import string
from odoo import models,fields

class servicios(models.Model):
    _name = 'motel.servicios'

    servicio = fields.Char(string='Servicio')
    vebidas = fields.Char(string='Vebidas')
    


    _sql_constraints = [
        ('unique_habitacion', 'unique (name)', 'la habitacion ya existe!')
    ]