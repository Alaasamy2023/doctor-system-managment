# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class doctor(models.Model):
    _name = 'dms.doctor'

    name = fields.Char("Name")
    email = fields.Char("email")
    address = fields.Char("address")
    phone = fields.Integer()
    fee = fields.Integer()
    specialization_id = fields.Many2one("dms.specialization")

