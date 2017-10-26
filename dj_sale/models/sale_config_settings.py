# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import models


class SaleConfigSettings(models.TransientModel):

    _inherit = 'sale.config.settings'

    # 'sale_note' is a text field but in most cases contains html
    _dj_file_fields_names = ('sale_note', )
