import logging
import unittest
import time
from testconfig import config
from framework.constructor import constructor


class OVC_BaseTest(constructor):

    env = config['main']['environment']
    location = config['main']['location']

    def __init__(self, *args, **kwargs):
        super(OVC_BaseTest, self).__init__(*args, **kwargs)
        self.vdcusers = [{'kheirj': {'provider': 'itsyouonline', 'email': 'kheirj@greenitglobe.com'}}]

    def lg(self, msg):
        self._logger.info(msg)

    def handle_blueprint(self, yaml, *args, **kwargs):
        kwargs['env'] = OVC_BaseTest.env
        kwargs['location'] = OVC_BaseTest.location
        blueprint = self.create_blueprint(yaml, **kwargs)
        self.execute_blueprint(blueprint)

    def create_account(self, *args, **kwargs):
        self.handle_blueprint('account.yaml', *args, **kwargs)

    def create_cs(self, *args, **kwargs):
        self.handle_blueprint('vdc.yaml', *args, **kwargs)

    def create_vm(self, *args, **kwargs):
        self.handle_blueprint('vm.yaml', *args, **kwargs)
