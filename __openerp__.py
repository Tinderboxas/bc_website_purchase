{
    'name': 'Online Proposals',
    'category': 'Website',
    'summary': 'Send Professional Quotations',
    'website': 'https://www.odoo.com/page/quote-builder',
    'version': '1.0',
    'description': """
Elmatica Style
=========================

        """,
    'author': 'OpenERP SA',
    'depends': ['website', 'mail', 'purchase', 'purchase_requisition'],
    'data': [
        'wizards/request_relevant_suppliers.xml',
        'views/website_quotation.xml',
        'views/website_quotation_backend.xml',
        #'views/report_saleorder.xml',
        'data/website_quotation_data.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'data/website_quotation_demo.xml'
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
}
