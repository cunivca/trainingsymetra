from odoo import models, fields, api

class stock_move(models.Model):
    _inherit = "stock.picking"

    planned_duration = fields.Integer(copy=False, string='Planned duration', compute='_count_planned_duration', store=True, help="Date difference between creation and scheduled date")

    @api.depends("scheduled_date", "create_date")
    def _count_planned_duration(self):
        for record in self:
            if record.scheduled_date and record.create_date:
                scheduled_round = record.scheduled_date.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
                create_round = record.create_date.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
                record.planned_duration = (scheduled_round - create_round).days
            else:
                record.planned_duration = False

    