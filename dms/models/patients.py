# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class patients(models.Model):
    _name = 'dms.patients'

    name = fields.Char("Name")
    email = fields.Char("email")
    address = fields.Char("address")
    phone = fields.Integer()
    age = fields.Integer()
    gender = fields.Selection([('m', "Male"), ('f', "Female")], default="m")

    patient_medical_id = fields.Many2many("dms.patient_medical")

