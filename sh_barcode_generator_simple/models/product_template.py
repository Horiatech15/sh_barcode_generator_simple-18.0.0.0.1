# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from . import sh_barcode
import base64
import werkzeug.exceptions
from odoo import  fields, models



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sh_product_barcode_img = fields.Binary(
        string="Barcode Image", readonly=True)

    def action_generate_barcode_image(self):
        self.ensure_one()
        if self.barcode:
            img_barcode = self.env['ir.actions.report'].barcode(
                'Code128', self.barcode, width=500, height=90, humanreadable=0)
            self.sh_product_barcode_img = base64.b64encode(img_barcode)

    def generate_barcode_image(self, ean):
        # generate Barcode image
        try:
            ean_barcode = self.env['ir.actions.report'].barcode(
                'EAN13', ean, width=500, height=90, humanreadable=0)
            if ean_barcode:
                self.sh_product_barcode_img = base64.b64encode(ean_barcode)

        except (ValueError, AttributeError):
            raise werkzeug.exceptions.HTTPException(
                description='Cannot convert into barcode.')

    def action_generate_barcode(self):
        if self:
            for rec in self:
                ean = sh_barcode.generate_ean(self.env.company.sh_barcode_type)
                rec.barcode = ean
                rec.generate_barcode_image(ean)
