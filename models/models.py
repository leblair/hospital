# -*- coding: utf-8 -*-
# from odoo import models, fields, api
from odoo import models, fields


class Patients(models.Model):
    _name = 'hospital.patient'
    _description = 'Pacient Record'

    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Integer(string='Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
