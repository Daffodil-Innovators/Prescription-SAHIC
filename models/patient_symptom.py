from odoo import models,fields

class PatientSymptoms(models.Model):
    _name = 'dsl.patient.symptom'
    _description = 'Patient Symptom'

    name = fields.Char(string='Symptom Name', required=True)
    code = fields.Char(string='Code',copy=False,readonly=True,default=lambda self: self.env['ir.sequence'].next_by_code('dsl.patient.symptom'))

    active = fields.Boolean(string='Active', default=True)
    note = fields.Text(string='Notes')
    body_organ_id = fields.Many2one('dsl.patient.body.organ',string="Body Organ",required=True)
