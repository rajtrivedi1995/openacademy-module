# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class MyWeb(http.Controller):
    @http.route('/myhomepage', auth='public', website=True)
    def index(self, **kw):
        # details=http.request.env['openacademy.registered.student'].sudo().search([])
        return http.request.render('openacademy.custom_homepage')
