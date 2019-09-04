from odoo import models, fields, api, _ 
from odoo.exceptions import ValidationError

class ReportLXT(models.TransientModel):

	_name = "wizard.reporte.lxt"

	route_report = fields.Many2one( 'pos.config' , string = 'Selecciona la ruta' )
	route_select = fields.Many2one( 'pos.session' , string = 'Ruta seleccionada' )

	@api.onchange('route_report')
	def _selectRoute(self):
		if self.route_report:
			search = self.env['pos.session'].search([('config_id','=',self.route_report.id)],limit=1)
			self.route_select = search.id
	
	def generate_report(self):
		self.ensure_one()
		if self.route_report:
			dom_rep = [('session_id','=',self.route_select.id)]
			busq = self.env['pos.order'].search([('session_id','=',self.route_select.id)],limit=1)
			if busq:	
				id_tree_view_point = self.env.ref('point_of_sale.view_pos_order_tree').id
				id_form_view_point = self.env.ref('point_of_sale.view_pos_pos_form').id
				action = {
					'type': 'ir.actions.act_window',
					'views': [(id_tree_view_point, 'tree'), (id_form_view_point, 'form')],
					'view_mode': 'tree,form',
					'name': _('Reporte de ' + str(self.route_report.name)),
					'res_model': 'pos.order',
					'domain' : dom_rep
				}
				return action
			else:
				raise ValidationError('La ruta seleccionada no tiene pedidos de venta creados.')
		else:
			raise ValidationError('Por favor seleccione una ruta para continuar...')