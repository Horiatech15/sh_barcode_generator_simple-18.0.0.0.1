# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import api, http, models
import base64


class ShIrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def webclient_rendering_context(self):
        res = super(ShIrHttp, self).webclient_rendering_context()
        company_image = self.env.company.favicon
        print("\n\n\n Company Image", company_image)
        base64_data = base64.b64encode(company_image).decode('utf-8')
        image_format = "x-icon"
        data_uri = f"data:image/{image_format};base64,{base64_data}"
        res['fav_icon'] = data_uri
        return res
