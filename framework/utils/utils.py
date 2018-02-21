import logging
import unittest
import time
from testconfig import config


class OVC_BaseTest(unittest.TestCase):

    env = config['main']['environment']
    location = config['main']['location']

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

    def handle_thread(self, yaml, *args, **kwargs):
        kwargs['env'] = OVC_BaseTest.env
        kwargs['location'] = OVC_BaseTest.location
        blueprint = self.create_blueprint(yaml, **kwargs)
        self.execute_blueprint(blueprint)

    def create_account(self, *args, **kwargs):
        self.handle_thread('account.yaml', *args, **kwargs)

    def create_cs(self, *args, **kwargs):
        self.handle_thread('account.yaml', *args, **kwargs)

    def create_vm(self, *args, **kwargs):
        self.handle_thread('account.yaml', *args, **kwargs)
