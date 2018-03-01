import logging
import unittest
import time
import os
from testconfig import config
from framework.constructor import constructor
from js9 import j


class OVC_BaseTest(constructor):

    env = config['main']['environment']
    key = config['main']['key']

    def __init__(self, *args, **kwargs):
        super(OVC_BaseTest, self).__init__(*args, **kwargs)
        self.ovc_client = self.ovc_client()

    def setUp(self):
        super(OVC_BaseTest, self).setUp()

    def iyo_jwt(self):
        key_path = os.path.expanduser(OVC_BaseTest.key)
        ito_client = j.clients.itsyouonline.get(instance="main", sshkey_path=key_path)
        return ito_client.jwt

    def ovc_client(self):
        key_path = os.path.expanduser(OVC_BaseTest.key)
        data = {'address': OVC_BaseTest.env,
                'port': 443,
                'appkey_': self.iyo_jwt()
                }
        return j.clients.openvcloud.get(instance='main', data=data,
                                        sshkey_path=key_path)

    def handle_blueprint(self, yaml, *args, **kwargs):
        kwargs['token'] = self.iyo_jwt()
        blueprint = self.create_blueprint(yaml, **kwargs)
        self.execute_blueprint(blueprint)

    def create_account(self, *args, **kwargs):
        self.handle_blueprint('account.yaml', *args, **kwargs)

    def create_cs(self, *args, **kwargs):
        self.handle_blueprint('vdc.yaml', *args, **kwargs)

    def create_vm(self, *args, **kwargs):
        self.handle_blueprint('vm.yaml', *args, **kwargs)

    def get_cloudspace(self, name):
        cloudspaces = self.ovc_client.api.cloudapi.cloudspaces.list()
        for cs in cloudspaces:
            if cs['name'] == name:
                return cs
        return False
