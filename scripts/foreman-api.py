#!/usr/bin/python

import sys
import os
import os.path

from restkit import Resource
from restkit import BasicAuth

import json

class ForemanResource(Resource):
    def __init__(self, url=None, pool_instance=None, **kwargs):
        super(Foreman, self).__init__(url, follow_redirect=True,
                                     max_follow_redirect=10,
                                     pool=pool_instance,
                                     **kwargs)
    def request(self, *args, **kwargs):
        headers = {'Content-Type':'application/json',
                   'Accept':'application/json'}
        kwargs['headers'] = headers
        resp = super(Foreman, self).request(*args, **kwargs)
        return json.loads(resp.body_string())

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


class ForemanHosts(object):
    def __init__(self, foreman_url=None, username=None, password=None):
        auth = BasicAuth(username, password)
        self._foreman = ForemanResource(foreman_url, filters=[auth])

    def list(self):
        return self._foreman.get('/hosts/')

    def search(self, search=''):
        query = {'search':search}
        return self._foreman.get('/hosts/', query)
    def get(self, fqdn):
        return self._foreman.get('/hosts/%s' % fqdn)


