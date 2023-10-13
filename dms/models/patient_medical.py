# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class patient_medical(models.Model):
    _name = 'dms.patient_medical'


    _rec_name ="petient_id"

    daily_dose = fields.Float()
    dose = fields.Float()
    start_time = fields.Datetime()
    end_time = fields.Datetime()
    status = fields.Selection([('active', "active"), ('completed', "completed")], default="active")



    doctor_id = fields.Many2one("dms.doctor")
    petient_id = fields.Many2one("dms.patients")
    medical_history_id = fields.Many2one("dms.medical_history")

