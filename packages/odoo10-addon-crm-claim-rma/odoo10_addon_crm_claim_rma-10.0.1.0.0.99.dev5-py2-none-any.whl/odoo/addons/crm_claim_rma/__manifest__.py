# -*- coding: utf-8 -*-
# © 2017 Techspawn Solutions
# © 2015 Vauxoo
# © 2015 Eezee-It
# © 2009-2013 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'RMA Claim (Product Return Management)',
    'version': '10.0.1.0.0',
    'category': 'Generic Modules/CRM & SRM',
    'author': "Akretion, Camptocamp, Eezee-it, MONK Software, Vauxoo, "
              "Techspawn Solutions, "
              "Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/rma',
    'license': 'AGPL-3',
    'depends': [
        'purchase',
        'sale',
        'sales_team',
        'stock',
        'crm_claim_rma_code',
        'crm_rma_location',
        'product_warranty',
    ],
    'data': [
        'data/ir_sequence_type.xml',
        'data/crm_team.xml',
        'data/crm_claim_category.xml',
        'views/account_invoice.xml',
        'wizards/claim_make_picking.xml',
        'views/crm_claim.xml',
        "views/claim_line.xml",
        'views/res_partner.xml',
        'views/stock_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
