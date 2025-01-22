# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import models,api

class IrActionsAction(models.Model):
    _inherit = 'ir.actions.act_window'

    def read(self, fields=None, load='_classic_read'):
        results = super(IrActionsAction, self).read(fields=fields, load=load)
        if not fields or 'help' in fields:
            # fetch debarnd name
            debrand_obj = self.env['sh.debranding.config'].sudo().search([
            ], limit=1)
            if debrand_obj:
                for res in results:
                    if isinstance(res, dict) and res.get('help'):
                        res['help'] = res['help'].replace(
                            'Odoo', debrand_obj.name)
        return results

