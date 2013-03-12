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
import json

try:
    from restkit import Resource
except ImportError as e:
    print('You didn\'t install python-restkit')
    print(e)
    sys.exit(1)

class ForemanResource(Resource):
    def __init__(self, url=None, pool_instance=None, **kwargs):
        super(ForemanResource, self).__init__(url, follow_redirect=True, max_follow_redirect=10, pool=pool_instance, **kwargs)

    def request(self, *args, **kwargs):
        headers = {
                'Content-Type':'application/json; charset=utf-8',
                'Accept':'application/json'
        }
        kwargs['headers'] = headers
        resp = super(ForemanResource, self).request(*args, **kwargs)
        return json.loads(resp.body_string())
