# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    generate_barcode_on_product = fields.Boolean(
        string="Generate Product Barcode On Product Create?")

    sh_barcode_type = fields.Selection([
        ('code128', 'Code 128'),
        ('code39', 'Code 39'),
        ('ean', 'EAN'),
        ('ean13', 'EAN-13'),
        ('ean8', 'EAN-8'),
        ('isbn10', 'ISBN10'),
        ('issn', 'ISSN'),
        ('pzn', 'PZN'),
        ('upca', 'UPCA')
    ], string='Barcode-Type (Product)', default='ean13')
