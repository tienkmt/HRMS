from customer_addons.hrms.models.constraint import Constraint
from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'res.users'

    name = fields.Char(string='Tên', required=True)
    block = fields.Many2one('block', required=True)
    position = fields.Selection()

    list_select = []

    @api.onchange('block')
    def _onchange_block(self):
        for rec in self:
            if rec.block.name == Constraint.block_office_name:
                list_select = [('admin', 'Admin'), ('manager_system', 'Manager System'), ()]
