# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
import time

class FormatDate(models.Model):

	_inherit = 'pos.order'

	def __init__(self, cr, uid, name, context=None):
		super(FormatDate, self).__init__(cr, uid, name, context=context)
		self.localcontext.update({
			"format_date" : self.format_date
		})

	def format_date(self, date):
		if date:
			return str(datetime.strptime(o.date_order,"%d/%m/%Y %H:%M %a").strftime("%d/%m/%Y %H:%M %a"))