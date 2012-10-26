# -*- coding: utf-8 -*-
###############################################################################
# python-foreman-api - Foreman API Python Library
# Copyright (C) 2012 Stephan Adig <sh@sourcecode.de>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
###############################################################################

import sys

try:
    from restkit import BasicAuth
except ImportError, e:
    print('You didn\'t install python-restkit library')
    print(e)
    sys.exit(1)

from resources import ForemanResource


class Foreman(object):
    def __init__(self, foreman_url=None, username=None, password=None):
        auth = BasicAuth(username, password)
        self._foreman = ForemanResource(foreman_url, filters=[auth])

    def list(self):
        pass

    def search(self, search=''):
        pass

    def get(self):
        pass

class FHosts(Foreman):
    def list(self):
        return self._foreman.get('/hosts/')

    def search(self, search=''):
        query = {'search':search}
        return self._foreman.get('/hosts/', params_dict=query)

    def get(self, fqdn):
        return self._foreman.get('/hosts/%s' % fqdn)


