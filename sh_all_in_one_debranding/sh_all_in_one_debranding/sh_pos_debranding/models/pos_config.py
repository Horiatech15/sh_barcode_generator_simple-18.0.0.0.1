# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import api, models
from lxml import etree

class POSConfig(models.Model):
    _inherit = "pos.config"

    @api.model
    def fields_view_get(self, view_id=None, view_type="form", toolbar=False, submenu=False):

        res = super().fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )

        page_name = res["name"]
        if not page_name == "pos.config.form.view":
            return res

        doc = etree.XML(res["arch"])
        enterprise_query = "//div[div[field[@widget='upgrade_boolean']]]"
        for item in doc.xpath(enterprise_query):
            item.set('style', 'display:none')

        res["arch"] = etree.tostring(doc)

class ShPosSession(models.Model):
    _inherit = "pos.session"
    @api.model
    def _load_pos_data_models(self, config_id):
        models = super()._load_pos_data_models(config_id)
        models += ['sh.debranding.config']
        return models