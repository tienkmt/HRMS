from odoo import models, fields


class departments(models.Model):
    _name = 'departments'
    _description = 'Phòng ban'

    name = fields.Char(string='Tên Phòng/Ban', required=True)
    hight_departments = fields.Many2one('departments', string='Phòng/Ban cấp trên')
    manager = fields.Many2one('res.users', string='Quản lý')
