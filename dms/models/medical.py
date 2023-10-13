# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class medical(models.Model):
    _name = 'dms.medical_history'

    name = fields.Char("Name")
    Effective_Material = fields.Char("Effective_Material")
    price = fields.Float()

