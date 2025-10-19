from odoo import models,fields

class PatientFindings(models.Model):
    _name = 'dsl.patient.findings'
    _description = 'Patient Findings'

    name = fields.Char(string='Findings Name', required=True)
    code = fields.Char(string='Code',copy=False,readonly=True,default=lambda self: self.env['ir.sequence'].next_by_code("dsl.patient.findings"))

    active = fields.Boolean(string='Active', default=True)
    note = fields.Text(string='Notes')
    body_organ_id = fields.Many2one('dsl.patient.body.organ',string="Body Organ",required=True)
