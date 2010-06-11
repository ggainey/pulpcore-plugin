#!/usr/bin/python
#
# Copyright (c) 2010 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.

import sys
import os

cdir = os.path.dirname(__file__)
sys.path.append(os.path.join(cdir, '../../src'))
sys.path.append(os.path.join(cdir, '../unit'))

from pulptools.connection import RepoConnection
from pulptools.connection import ConsumerConnection
from pulptools.connection import PackageConnection
from pulptools.connection import PackageGroupConnection
from pulptools.connection import PackageGroupCategoryConnection

from test_api import TestApi, TestConfig

class RemoteTestApi(TestApi):
    """
    This class subclasses TestApi and overrides the API handlers to actually
    use the same classes the CLI uses.  This ensures we are using the API exactly
    like we are when we call the pulp python API directly.
    
    The overridden testcases in this class indicate tests that *dont* pass yet.
    """

    def setUp(self):
        d = dict(host='localhost', port=8811)
        self.config = TestConfig()
        self.rapi = RepoConnection(**d)
        self.capi = ConsumerConnection(**d)
        self.papi = PackageConnection(**d)
        self.pgapi = PackageGroupConnection(**d)
        self.pgcapi = PackageGroupCategoryConnection(**d)
        
    def test_bulk_create(self):
        pass

    def test_json(self):
        pass

    def test_sync_two_repos_share_common_package(self):
        pass

    def test_sync_two_repos_share_common_package(self):
        pass

    def test_sync(self):
        pass

    def test_local_sync(self):
        pass

    def test_packages(self):
        pass

    def test_package_groups(self):
        pass

    def test_package_group_categories(self):
        pass
