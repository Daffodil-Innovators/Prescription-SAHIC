{
    "name": "Sahic Prescription Extension",
    "description": """
        Prescription Extension For Sahic.
    """,
    'version': '14.0.1.0',
    'category': 'AI',
    'author': 'Daffodil Software Limited',
    'support': 'https://daffodil-bd.com',
    'website': 'https://daffodil-bd.com',
    "depends": ["base", "dsl_prescription_extension", "dsl_hms_physiotherapy"],
    "data": [
        "security/ir.model.access.csv",
        'data/ir_sequence.xml',
        'data/body_organ_data.xml',
        'data/findings_data.xml',
        'data/symptom_data.xml',
        "report/prescription.xml",
        "views/dsl_therapy_view_inherited_prescirption_extension.xml",
        "views/patient_body_organ_views.xml",
        "views/patient_findings_views.xml",
        "views/patient_symptom_views.xml",
        "views/menus.xml",

    ],
    'sequence': 4,
    'installable': True,
    'application': False,
    'contributors': [
        'Md. Farhan Afsar <https://github.com/Farhan-Afsar>',
    ],
}
