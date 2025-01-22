# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

# from lxml import html as htmltree
# from lxml import etree

# import re
from odoo import models, tools
from markupsafe import Markup


class MailRenderMixin(models.AbstractModel):
    _inherit = 'mail.render.mixin'

    def _replace_local_links(self, html, base_url=None):
        """ Replace local links by absolute links. It is required in various
        cases, for example when sending emails on chatter or sending mass
        mailings. It replaces

         * href of links (mailto will not match the regex)
         * src of images (base64 hardcoded data will not match the regex)
         * styling using url like background-image: url

        It is done using regex because it is shorten than using an html parser
        to create a potentially complex soupe and hope to have a result that
        has not been harmed.
        """
        if not html:
            return html

        wrapper = Markup if isinstance(html, Markup) else str
        html = tools.ustr(html)
        if isinstance(html, Markup):
            wrapper = Markup
