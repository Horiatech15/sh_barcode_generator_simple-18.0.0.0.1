# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import api, fields, models
from lxml import etree


class Users(models.Model):
    """ Update of res.users class
        - add a preference about sending emails about notifications
        - make a new user follow itself
        - add a welcome message
        - add suggestion preference
        - if adding groups to an user, check mail.channels linked to this user
    """
    _inherit = 'res.users'

    notification_type = fields.Selection([
        ('email', 'Handle by Emails'),
        ('inbox', 'Handle in Company')],
        'Notification Management', required=True, default='email',
        help="Policy on how to handle Chatter notifications:\n"
             "- Emails: notifications are sent to your email\n"
             "- Planet Odoo: notifications appear in your Planet Odoo Inbox")


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    @api.model
    def fields_view_get(self, view_id=None, view_type="form", toolbar=False, submenu=False):

        res = super(ResConfigSettings, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )

        page_name = res["name"]
        if not page_name == "res.config.settings.view.form":
            return res

        doc = etree.XML(res["arch"])
        enterprise_query = "//div[div[field[@widget='upgrade_boolean']]]"
        for item in doc.xpath(enterprise_query):
            item.set('style', 'display:none')

        res["arch"] = etree.tostring(doc)
        return res
