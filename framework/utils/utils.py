import logging
import unittest
import uuid
import time
import signal
import os

class OVC_BaseTest(unittest.TestCase):

    url = 'be-g8-4' # get it from the config

    def __init__(self, *args, **kwargs):
        # ovc object variables the class need to be aware about.
        #for k in kwargs:
        #    setattr(self, k, kwargs[k])
        #self.csname = self.random_string()
        super(OVC_BaseTest, self).__init__(*args, **kwargs)
        self._testID = self._testMethodName
        self._startTime = time.time()
        self._logger = logging.LoggerAdapter(logging.getLogger('openvcloud_testsuite'),
                                             {'testid': self.shortDescription() or self._testID})
        self.templatespath = './framework/utils/templates'

    def lg(self, msg):
        self._logger.info(msg)

    def execute_bp(self):
        os.system('zrobot blueprint execute /root/blueprints/bp.yaml')

    def create_account(self, accountname):
        pass

    def create_cs(self, *args, **kwargs):
        self.__init__(*args, **kwargs)
        self.create_blueprint('test.yaml')

    def create_vm(self, vmname):
        pass
