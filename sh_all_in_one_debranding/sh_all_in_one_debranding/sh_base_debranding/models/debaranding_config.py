# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models , api


class DebrandingConfig(models.Model):
    _name = 'sh.debranding.config'
    _description = 'Debranding Configuration'

    name = fields.Char("App Name", default="Softhealer")
    url = fields.Char("App URL")
    bot_user = fields.Char('Bot User')
    bot_user_login = fields.Char("Bot User Login")
    # favicon = fields.Binary(string="Company Favicon",
    #                         help="This field holds the image used to display a favicon for a given company.")
    avatar = fields.Binary(
        string="Avatar Image", help="This field holds the image used to display a Avatar.")

    show_support_url = fields.Boolean("Support URL ?")
    show_account_url = fields.Boolean("Account URL ?")
    show_doc_url = fields.Boolean("Documentation URL ?")

    support_url = fields.Char("Support URL")
    doc_url = fields.Char("Documentation URL")
    online_url = fields.Char("Account URL")

    def write(self, vals):
        res = super(DebrandingConfig, self).write(vals)
        if vals.get('avatar', False):
            bot_user = self.env['res.users'].sudo().search(
                [('id', '=', 1), ('active', '=', False)])
            bot_user.write({'image_1920': vals.get('avatar')})

        if vals.get('bot_user') or vals.get('bot_user_login'):
            # self._cr.execute("Update res_users set login='%s' where id=1;Update res_partner set email='%s',name='%s',display_name='%s' where id=2;" % (
                # self.bot_user_login, self.bot_user_login, self.bot_user, self.bot_user,))
            
            self._cr.execute("Update res_users set login='%s' where id=1;Update res_partner set email='%s',name='%s' where id=2;" % (
                self.bot_user_login, self.bot_user_login, self.bot_user))

        
        return res

    @api.model
    def _load_pos_data_domain(self, data):
        return []
    
    @api.model
    def _load_pos_data_fields(self, config_id):
        return []

    @api.model
    def _load_pos_data(self, data):
        domain = self._load_pos_data_domain(data)
        fields = self._load_pos_data_fields(data['pos.config']['data'][0]['id'])
        return {
            'data': self.search_read(domain, fields, load=False) if domain is not False else [],
            'fields': fields,
        }