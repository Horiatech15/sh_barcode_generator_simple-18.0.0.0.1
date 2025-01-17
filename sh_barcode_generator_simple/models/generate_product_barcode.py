# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from . import sh_barcode
# import base64
from odoo import fields, models,_
from odoo.exceptions import UserError


class GenerateProductBarcode(models.Model):
    _name = 'generate.product.barcode'
    _description = 'Generate Product Barcode'

    # Generate Barcode for Existing Product
    overwrite_existing = fields.Boolean("Overwrite Barcode If Exists")

    def generate_barcode(self):
        if self.env.user.has_groups('sh_barcode_generator_simple.group_barcode_generator'):

            context = dict(self._context or {})
            active_ids = context.get('active_ids', []) or []
            active_model = context.get('active_model', []) or []

            if active_model == 'product.product':
                for record in self.env['product.product'].browse(active_ids):

                    new_barcode = ''
                    if record.id:
                        new_barcode = sh_barcode.generate_ean(
                            self.env.company.sh_barcode_type)
                        if self.overwrite_existing:  # Overwrite existing
                            record.barcode = new_barcode
                            record.generate_barcode_image(new_barcode)
                        else:
                            if not record.barcode:  # If barcode exists,then don't overwrite, Else generate New
                                record.barcode = new_barcode
                                record.generate_barcode_image(new_barcode)

            elif active_model == 'product.template':
                for record in self.env['product.template'].browse(active_ids):
                    new_barcode = ''
                    if record.id:
                        new_barcode = sh_barcode.generate_ean(
                            self.env.company.sh_barcode_type)
                        if self.overwrite_existing:  # Overwrite existing
                            record.barcode = new_barcode
                            record.generate_barcode_image(new_barcode)
                        else:
                            if not record.barcode:  # If barcode exists,then don't overwrite, Else generate New
                                record.barcode = new_barcode
                                record.generate_barcode_image(new_barcode)

            return {'type': 'ir.actions.act_window_close'}

        else:
            raise UserError(
                _("You don't have rights to generate product barcode"))
