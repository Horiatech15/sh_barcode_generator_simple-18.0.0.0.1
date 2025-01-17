# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from . import sh_barcode
import base64
import werkzeug.exceptions
from odoo import  api, models


class ShProductProduct(models.Model):
    _inherit = 'product.product'

    def action_generate_barcode_image(self):
        self.ensure_one()
        if self.barcode:
            img_barcode = self.env['ir.actions.report'].barcode(
                'Code128', self.barcode, width=500, height=90, humanreadable=0)
            self.sh_product_barcode_img = base64.b64encode(img_barcode)

    def action_generate_barcode(self):
        if self:
            for rec in self:
                ean = sh_barcode.generate_ean(self.env.company.sh_barcode_type)
                rec.barcode = ean
                rec.generate_barcode_image(ean)

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

    @api.model_create_multi
    def create(self, vals_list):
        res = super(ShProductProduct, self).create(vals_list)
        if self.env.user.has_groups('sh_barcode_generator_simple.group_barcode_generator') and self.env.company.generate_barcode_on_product:
            # Filter out no barcode products
            barcode_not_generated_product = res.filtered(
                lambda product: not product.barcode)
            for product in barcode_not_generated_product:
                # generate product barcode
                ean = sh_barcode.generate_ean(self.env.company.sh_barcode_type)
                product.barcode = ean
                product.generate_barcode_image(ean)

        return res
