# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_sale_order_all_done(self):
        self.action_confirm()

        for picking in self.picking_ids:

            for line in picking.move_lines:
                line.quantity_done = line.product_uom_qty

            picking.button_validate()

