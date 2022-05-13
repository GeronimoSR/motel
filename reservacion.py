# -*- coding: utf-8 -*-
from odoo import models,fields,api

class inscripciones(models.Model):
    _name = 'motel.reservacion'

    huespedes = fields.Many2one('motel.huespedes', string='Huespedes')
    habitaciones = fields.Many2one('motel.habitaciones',string='Habitaciones')
    servicios = fields.Many2one('motel.servicios',string='Servicios')
    

    _sql_constraints = [
        ('unique_reservaciones', 'unique(habitaciones)', 'la reservacion esta ocupada!')
    ]