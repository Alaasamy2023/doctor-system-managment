# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class specialization(models.Model):
    _name = 'dms.specialization'

    _rec_name ="specialization"

    specialization = fields.Char("specialization")
    is_open = fields.Boolean()


