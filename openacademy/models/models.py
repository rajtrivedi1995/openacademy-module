# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

class openacademy(models.Model):
    _name = 'openacademy.openacademy'
    _description = "OpenAcademy OpenAcademy"

    name = fields.Char()

class SaleOrder(models.Model):
    _inherit = "sale.order"
