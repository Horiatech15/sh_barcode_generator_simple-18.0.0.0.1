from odoo import http
from odoo.addons.web.controllers import main as main
from odoo.http import request
import functools
from odoo.tools.mimetypes import guess_mimetype
import base64
import io
from odoo.modules import get_resource_path

try:
    from werkzeug.utils import send_file
except ImportError:
    from odoo.tools._vendor.send_file import send_file

import odoo
import odoo.modules.registry

#----------------------------------------------------------
# Odoo Web web Controllers
#----------------------------------------------------------
class Home(http.Controller):

    @http.route([
        '/company_url',
    ], type='http', auth="none", cors="*")
    def company_url(self, dbname=None, **kw):
        debrand_obj = request.env['sh.debranding.config'].sudo().search([],limit=1)
        redirect = '/web'
        if debrand_obj:
            redirect = debrand_obj.url
        return request.redirect(redirect)

    @http.route([
        '/web/binary/company_logo',
        '/logo',
        '/logo.png',
    ], type='http', auth="none", cors="*")
    def company_logo(self, dbname=None, **kw):
        imgname = 'logo'
        imgext = '.png'
        placeholder = functools.partial(get_resource_path, 'sh_backend_debranding', 'static', 'src', 'img')
        dbname = request.db
        uid = (request.session.uid if dbname else None) or odoo.SUPERUSER_ID

        if not dbname:
            response = http.Stream.from_path(placeholder(imgname + imgext)).get_response()
        else:
            try:
                # create an empty registry
                registry = odoo.modules.registry.Registry(dbname)
                with registry.cursor() as cr:
                    company = int(kw['company']) if kw and kw.get('company') else False
                    if company:
                        cr.execute("""SELECT logo_web, write_date
                                        FROM res_company
                                       WHERE id = %s
                                   """, (company,))
                    else:
                        cr.execute("""SELECT c.logo_web, c.write_date
                                        FROM res_users u
                                   LEFT JOIN res_company c
                                          ON c.id = u.company_id
                                       WHERE u.id = %s
                                   """, (uid,))
                    row = cr.fetchone()
                    if row and row[0]:
                        image_base64 = base64.b64decode(row[0])
                        image_data = io.BytesIO(image_base64)
                        mimetype = guess_mimetype(image_base64, default='image/png')
                        imgext = '.' + mimetype.split('/')[1]
                        if imgext == '.svg+xml':
                            imgext = '.svg'
                        response = send_file(image_data, request.httprequest.environ,
                                             download_name=imgname + imgext, mimetype=mimetype, last_modified=row[1])
                    else:
                        response = http.Stream.from_path(placeholder('nologo.png')).get_response()
            except Exception:
                response = http.Stream.from_path(placeholder(imgname + imgext)).get_response()
        return response
