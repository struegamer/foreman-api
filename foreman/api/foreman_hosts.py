# -*- coding: utf-8 -*-
###############################################################################
#
#    (DC)² - DataCenter Deployment Control
#    Copyright (C) 2010, 2011, 2012  Stephan Adig <sh@sourcecode.de>
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
###############################################################################

import sys

try:
    from restkit import BasicAuth
    from restkit.errors import ResourceNotFound

except ImportError, e:
    print('You didn\'t install python-restkit library')
    print(e)
    sys.exit(1)

from resources import ForemanResource
from foreman_main import Foreman


class ForemanHosts(Foreman):
    FOREMAN_RESOURCE = '/hosts/'

    def list(self):
        return self._foreman.get(self.FOREMAN_RESOURCE)

    def search(self, search=''):
        query = {'search':search}
        return self._foreman.get(self.FOREMAN_RESOURCE, params_dict=query)

    def get(self, fqdn):
        try:
            host = self._foreman.get('{0}{1}'.format(self.FOREMAN_RESOURCE, fqdn))
            return host
        except ResourceNotFound as e:
            return None

class ForemanHostFacts(Foreman):
    FOREMAN_RESOURCE = '/hosts/'

    def get(self, fqdn):
        try:
            host_facts = self._foreman.get('{0}{1}/facts'.format(self.FOREMAN_RESOURCE, fqdn))
            return host_facts
        except ResourceNotFound as e:
            return None

