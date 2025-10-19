from odoo import models,fields,api

class Therapy(models.Model):
    _inherit = 'prescription.order'

    is_therapy = fields.Boolean(string="Need Therapy?", default=False )

    physiotherapy_ids = fields.One2many(
        'dsl.physiotherapy',
        string='Physiotherapy Records',
        compute='_compute_physiotherapy_ids',
        store = False,
    )
    # symptom_ids = fields.Many2many('dsl.prescription.symptom', string="Symptom")

    symptom_ids = fields.Many2many(
        'dsl.patient.symptom',
        string='Symptoms',
    )
    findings_ids = fields.Many2many(
        'dsl.patient.findings',
        string='Findings',
    )

    @api.depends('patient_id')
    def _compute_physiotherapy_ids(self):
        for record in self:
            if record.patient_id:
                physiotherapy_records = self.env['dsl.physiotherapy'].search([
                    ('patient_id', '=', record.patient_id.id)
                ], order='date desc')

                record.physiotherapy_ids = physiotherapy_records
            else:
                record.physiotherapy_ids = self.env['dsl.physiotherapy'].browse([])


# class PrescriptionSymptom(models.Model):
#     _name = 'dsl.prescription.symptom'
#     _description = 'Prescription Symptom'
#
#     active = fields.Boolean(string='Active', default=True,invisible=True)
#     symptom_id = fields.Many2one('dsl.patient.symptom', string='Symptom', required=True)
#     prescription_id = fields.Many2one('prescription.order', string='Prescription', required=True, ondelete='cascade')


