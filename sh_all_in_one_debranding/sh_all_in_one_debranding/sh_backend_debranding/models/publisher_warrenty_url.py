# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models
from odoo.release import version_info


class PublisherWarrantyContract(models.AbstractModel):
    _inherit = 'publisher_warranty.contract'

    def update_notification(self, cron_mode=True):
        is_enterprise = version_info[5] == 'e'
        debrand_obj = self.env['sh.debranding.config'].sudo().search([
        ], limit=1)
        if is_enterprise or not debrand_obj:
            return super(PublisherWarrantyContract, self).update_notification(cron_mode)
        else:
            return True

