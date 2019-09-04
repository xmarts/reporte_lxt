# -*- coding: utf-8 -*-
from odoo import http

# class ReporteLxt(http.Controller):
#     @http.route('/reporte__lxt/reporte__lxt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reporte__lxt/reporte__lxt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reporte__lxt.listing', {
#             'root': '/reporte__lxt/reporte__lxt',
#             'objects': http.request.env['reporte__lxt.reporte__lxt'].search([]),
#         })

#     @http.route('/reporte__lxt/reporte__lxt/objects/<model("reporte__lxt.reporte__lxt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reporte__lxt.object', {
#             'object': obj
#         })