# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models
from .ir_model import debrand
from lxml import etree

class View(models.Model):
    _inherit = 'ir.ui.view'


    def postprocess_and_fields(self, node, model=None, **options):
        self and self.ensure_one()      # self is at most one view

        name_manager = self._postprocess_view(node, model or self.model, **options)

        arch = etree.tostring(node, encoding="unicode").replace('\t', '')
        arch = debrand(self.env,arch, is_code=True)

        models = {}
        name_managers = [name_manager]
        for name_manager in name_managers:
            models.setdefault(name_manager.model._name, set()).update(name_manager.available_fields)
            name_managers.extend(name_manager.children)
        return arch, models
