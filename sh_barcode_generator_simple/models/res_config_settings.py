# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    generate_barcode_on_product = fields.Boolean(
        string="Generate Product Barcode On Product Create?",
        related="company_id.generate_barcode_on_product",
        readonly=False,
    )

    sh_barcode_type = fields.Selection(
        related="company_id.sh_barcode_type",
        string="Barcode-Type (Product)",
        readonly=False,
    )
