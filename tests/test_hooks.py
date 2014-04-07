# -*- coding: utf-8 -*-
##
## This file is part of Invenio-Kwalitee
## Copyright (C) 2014 CERN.
##
## Invenio-Kwalitee is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio-Kwalitee is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio-Kwalitee; if not, write to the Free Software Foundation,
## Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
##
## In applying this licence, CERN does not waive the privileges and immunities
## granted to it by virtue of its status as an Intergovernmental Organization
## or submit itself to any jurisdiction.


import os
import tempfile
import shutil

from unittest import TestCase

from invenio_kwalitee.hooks import check_files, check_commit_message, \
    prepare_commit_msg_hook, commit_msg_hook, post_commit_hook, \
    pre_commit_hook


class HooksTest(TestCase):
    def setUp(self):
        self.path = tempfile.mkdtemp()
        os.system("cd %s && git init" % self.path)
        os.system("cd %s && echo 'pass' > test.py" % self.path)
        os.system("cd %s && git add test.py" % self.path)
        os.system("cd %s && git commit -m 'test'" % self.path)
        os.chdir(self.path)

    def tearDown(self):
        shutil.rmtree(self.path)

    def test_pre_commit_hook(self):
        pre_commit_hook()
