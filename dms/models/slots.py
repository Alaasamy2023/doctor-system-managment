# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class slots(models.Model):
    _name = 'dms.slots'

    slots = fields.Char("slots")


