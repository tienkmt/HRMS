from odoo import models, fields, api, exceptions


class Block(models.Model):
    _name = 'block'
    _description = ''

    name = fields.Char(string='Tên khối', required=True)
    description = fields.Text(string='Mô tả', default='')
    active = fields.Boolean(string='Hoạt động', default=True)
    has_change = fields.Boolean()

    @api.model
    def _auto_init(self):
        super(Block, self)._auto_init()
        existing_records = self.env['block'].search([('has_change', '=', False)])
        if len(existing_records) == 0:
            self._default_value_ofice()
            self._default_value_trade()
        elif len(existing_records) == 1:
            for rec in existing_records:
                if rec.name == 'Văn phòng':
                    self._default_value_trade()
                else:
                    self._default_value_ofice()

    def _default_value_ofice(self):
        self.create({
            'name': 'Văn phòng',
            'description': 'Khối văn phòng',
            'active': '1',
            'has_change': False
        })

    def _default_value_trade(self):
        self.create({
            'name': 'Thương mại',
            'description': 'Khối thương mại',
            'active': '1',
            'has_change': False
        })
