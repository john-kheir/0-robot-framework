import unittest
import uuid
import random
import time
from zerorobot.dsl.ZeroRobotAPI import ZeroRobotAPI
from framework.constructor import constructor


class BasicTests(constructor):
    # we can put this on __init__.py
    def __init__(self, *args, **kwargs):
        self.templatespath = './framework/utils/templates'
        super(BasicTests, self).__init__(*args, **kwargs)

    def setUp(self):
        self.api = ZeroRobotAPI()

    def test001_reboot_vm(self):
        """ OVC-001
        *Test case for reboot machine with different initial status (Running/Halted).*

        **Test Scenario:**

        #. create virtual machine vm, should succeed
        #. set the vm to required status, should succeed
        #. reboot machine with initial status, should succeed
        """
        self.lg('%s STARTED' % self._testID)

        # create blueprint
        text = self.create_cs(url='be-g8-4.demo.greenitglobe.com',
                              user='asdasdasd',
                              groups=['level1', 'admin'],
                              repeat=[2, 2],
                              accountname='john',
                              login='john',
                              csname='johnvdc')

        import ipdb;ipdb.set_trace()
        # execute blueprint
        self.execute_bp()

        # verify the data
        service = self.api.services.names['azmyvdc']
        state = {}
        while state == {}:
            state = service.state.categories

        state = service.state.categories['acitons']['install']
        self.assertEqual(state, 'ok')

        self.lg('%s ENDED' % self._testID)
