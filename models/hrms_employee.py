from customer_addons.hrms.models.hrms_constraint import Constraint
from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'res.users'

    name = fields.Char(string='Tên', required=True)
    block = fields.Many2one('block', required=True)
    list_select = []
    position = fields.Selection(list_select, string='Vị trí', required=True)

    @api.onchange('block')
    def _onchange_block(self):
        for rec in self:
            if rec.block.name == Constraint.BLOCK_OFFICE_NAME:
                list_select = [('admin', 'Admin'), ('manager_system', 'Quản lý hệ thống'),
                               ('manager_company', 'Quản lý công ty')]
            else:
                list_select = [('lead', 'Trưởng nhóm'), ('manager', 'Quản lý hệ thống'),
                               ('director', 'Giám đốc')]
