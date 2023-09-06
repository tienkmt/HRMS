from odoo import fields, models


class System(models.Model):
    _name = "hrms.system"
    _rec_name = "display_name"

    display_name = fields.Char(compute="", readonly=True)
    name_system = fields.Char(string="Tên hệ thống", required=True)
    parent_name = fields.Char(string="Hệ thống cha")
    type_system = fields.Selection([("sale", "Sale"), ("resale", "Resale")], string="Loại hệ thống", required=True)
    number_phone = fields.Char(string="Số điện thoại", size=10)
    chairman = fields.Selection(string="Chủ tịch")
    vice_chairman = fields.Selection(string="Phó chủ tịch")
    active = fields.Boolean("Hoạt động")
