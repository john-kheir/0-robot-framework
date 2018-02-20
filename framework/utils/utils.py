import logging
import unittest
import uuid
import time
import signal
from zerorobot import cli
import os

class OVC_BaseTest(unittest.TestCase):

    url = 'be-g8-4' # get it from the config

    def __init__(self, *args, **kwargs):
        super(OVC_BaseTest, self).__init__(*args, **kwargs)
        self.templatespath = './framework/utils/templates'
        # ovc object variables the class need to be aware about.
        #for k in kwargs:
        #    setattr(self, k, kwargs[k])
        #self.csname = self.random_string()

    def setUp(self):
        self._testID = self._testMethodName
        self._startTime = time.time()
        self._logger = logging.LoggerAdapter(logging.getLogger('openvcloud_testsuite'),
                                             {'testid': self.shortDescription() or self._testID})

    def execute_bp(self):
        os.system('zrobot blueprint execute /root/blueprints/bp.yaml')

    def create_account(self, accountname):
        pass

    def create_cs(self, **kwargs):
        self.__init__(**kwargs)
        self.create_blueprint('test.yaml')

    def create_vm(self, vmname):
        pass
