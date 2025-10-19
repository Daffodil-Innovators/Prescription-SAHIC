from odoo import models,fields

class PatientBodyOrgan(models.Model):
    _name = 'dsl.patient.body.organ'
    _description = 'Patient Body Organ'

    name = fields.Char(string='Organ Name', required=True)
    code = fields.Char(string='Code',copy=False,readonly=True,default=lambda self: self.env['ir.sequence'].next_by_code("dsl.patient.body.organ"))

    active = fields.Boolean(string='Active', default=True)
    note = fields.Text(string='Notes')
