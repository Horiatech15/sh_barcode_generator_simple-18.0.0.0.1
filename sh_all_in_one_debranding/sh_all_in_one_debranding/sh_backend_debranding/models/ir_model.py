import re
from odoo import api
from odoo import models
from odoo import tools


def debrand_documentation_links(source, new_documentation_website):
    return re.sub(r'https://www.odoo.com/documentation/',
                  str(new_documentation_website) + 'documentation/',
                  source, flags=re.IGNORECASE)


def debrand_links(source, new_website):
    return re.sub(r'\bodoo.com\b', new_website, source, flags=re.IGNORECASE)


def debrand(env, source, is_code=False):
    if not source or not re.search(r'\bodoo\b', source, re.IGNORECASE):
        return source

    new_name = "Softhealer"
    new_website = "softhealer.com"
    new_documentation_website = "softhealer.com"

    debrand_obj = env['sh.debranding.config'].sudo().search([], limit=1)
    if debrand_obj:
        new_name = debrand_obj.name
        new_website = debrand_obj.url
        new_documentation_website = debrand_obj.doc_url

    source = debrand_documentation_links(source, new_documentation_website)

    source = debrand_links(source, new_website)
    source = re.sub(
        r'\b(?<!\.)odoo(?!\.\S|\s?=|\w|\[)\b', new_name, source, flags=re.IGNORECASE)

    return source


def debrand_bytes(env, source):
    return bytes(debrand(env, source.decode('utf-8')), 'utf-8')


class IrModel(models.Model):
    _inherit = 'ir.model'

    @api.model
    def _debrand_dict(self, res):
        for k in res:
            res[k] = self._debrand(res[k])
        return res

    @api.model
    def _debrand(self, source):
        return debrand(self.env, source)

    @api.model
    @tools.ormcache_context('model_name', keys=('lang',))
    def get_field_string(self, model_name):
        res = super(IrModel, self).get_field_string(model_name)
        return self._debrand_dict(res)

    @api.model
    @tools.ormcache_context('model_name', keys=('lang',))
    def get_field_help(self, model_name):
        res = super(IrModel, self).get_field_help(model_name)
        return self._debrand_dict(res)

    @api.model
    @tools.ormcache_context('model_name', 'field_name', keys=('lang',))
    def get_field_selection(self, model_name, field_name):
        res = super(IrModel, self).get_field_selection(model_name)
        return self._debrand_dict(res)
