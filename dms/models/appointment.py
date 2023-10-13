# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class appointment(models.Model):
    _name = 'dms.appointment'

    name = fields.Char("name")
    petient_id = fields.Many2one("dms.patients")
    specialization_id = fields.Many2one("dms.specialization")
    doctor_id = fields.Many2one("dms.doctor")

    # related fields
    consultancy_fee = fields.Integer(related="doctor_id.fee")

    appointment_date = fields.Date()
    appointment_time = fields.Datetime()
    status = fields.Selection([('active', "active"), ('completed', "completed"), ('cancelled', "cancelled")], default="active")



