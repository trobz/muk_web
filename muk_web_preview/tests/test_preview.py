# -*- coding: utf-8 -*-

###################################################################################
#
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

import os
import base64
import logging
import unittest

from odoo import _
from odoo.tests import common

class PreviewTestCase(common.HttpCase):
    
    at_install = False
    post_install = True
    
    def setUp(self):
        super(PreviewTestCase, self).setUp()

    def tearDown(self):
        super(PreviewTestCase, self).tearDown()
        
    @unittest.skip()
    def test_preview(self):
        self.phantom_js("/web",
                        "odoo.__DEBUG__.services['web_tour.tour'].run('preview')",
                        "odoo.__DEBUG__.services['web_tour.tour'].tours.preview.ready",
                        login="admin")
        