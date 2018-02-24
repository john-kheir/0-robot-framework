import unittest
import uuid
import random
import time
from zerorobot.dsl.ZeroRobotAPI import ZeroRobotAPI
from framework.constructor import constructor
from collections import OrderedDict


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
        blueprint = self.create_account(accountname='johnnew',
                                        temp_actions={'account': ['install'], 'vdcuser': ['install']},)

        self.acc1 = self.random_string()
        self.cs1 = self.random_string()
        self.cs2 = self.random_string()
        self.vdcuser = self.random_string()
        vdcusers = [{self.vdcuser: {'provider': 'itsyouonline', 'email': 'kheirj@greenitglobe.com'}}]
        accounts = [{self.acc1: {}}]
        cloudspaces = [{self.cs1: {}},
                       {self.cs2: OrderedDict([('name', self.vdcuser), ('accesstype': 'CXDRAU')])}]
        self.createvdc(accounts=accounts, cloudspaces=cloudspaces)

        # verify the data
        service = self.api.services.names['johnnew']
        state = {}
        while state == {}:
            time.sleep(3)
            state = service.state.categories

        state = service.state.categories['actions']['install']
        self.assertEqual(state, 'ok')

        self.lg('%s ENDED' % self._testID)
