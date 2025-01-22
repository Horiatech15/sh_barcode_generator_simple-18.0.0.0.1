# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from . import sh_backend_debranding
from . import sh_base_debranding
from . import sh_pos_debranding
from . import sh_website_debranding
import base64

from odoo import api
from odoo import SUPERUSER_ID
from odoo import modules

def get_default_img():
    with open(modules.get_module_resource('sh_base_debranding', 'static/img', 'sh.png'),
              'rb') as f:
        return base64.b64encode(f.read())


def post_init_hook(env):
    bot_user = env['res.users'].sudo().search([('id', '=', 1)])
    bot_user.write({'image_1920': get_default_img})
    env.cr.execute("Update res_users set login='system@example.com' where id=1;Update res_partner set email='system@example.com',name='System User' where id=2;")