# -*- coding: utf-8 -*-
###############################################################################
#
#    foreman-api - python foreman api wrapper
#    Copyright (C) 2010, 2011, 2012, 2013  Stephan Adig <sh@sourcecode.de>
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

class ForemanEnvironment(Foreman):
    FOREMAN_RESOURCE = '/environments/'

    def list(self):
        return self._foreman.get(self.FOREMAN_RESOURCE)

    def get(self, **kwargs):
        try:
            environment = None
            if kwargs.get('id', None) is not None:
                environment = self._foreman.get('{0}{1}'.format(self.FORMAN_RESOURCE, kwargs.get('id', None)))
            if kwargs.get('environment', None) is not None:
                environment = self._foreman.get('{0}{1}'.format(self.FORMAN_RESOURCE, kwargs.get('environment', None)))
            return environment
        except ResourceNotFound as e:
            return None
