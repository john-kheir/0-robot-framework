import time
from zerorobot.dsl.ZeroRobotAPI import ZeroRobotAPI
from framework.utils.utils import OVC_BaseTest
from collections import OrderedDict


class BasicTests(OVC_BaseTest):
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
        self.log('%s STARTED' % self._testID)

        # create blueprint

        self.acc1 = self.random_string()
        self.cs1 = self.random_string()
        self.cs2 = self.random_string()
        self.vdcuser = self.random_string()
        self.vdcusers.extend([{self.vdcuser: {'provider': 'itsyouonline', 'email': 'muhamada@greenitglobe.com'}}])
        self.accounts = [{self.acc1: {}}]
        self.cloudspaces = [{self.cs1: {}},
                       {self.cs2: {'users': OrderedDict([('name', self.vdcuser), ('accesstype', 'CXDRAU')])}}]
        self.temp_actions = {'account': ['install'], 'vdcuser': ['install'], 'vdc': ['install']}
        self.create_cs(vdcusers=self.vdcusers, accounts=self.accounts,
                       cloudspaces=self.cloudspaces, temp_actions=self.temp_actions)

        # verify the data
        service = self.api.services.names[self.cs2]
        state = {}
        while state == {}:
            time.sleep(3)
            state = service.state.categories

        state = service.state.categories['actions']['install']
        self.assertEqual(state, 'ok')

        import ipdb;ipdb.set_trace()
        self.ovc_client


        self.log('%s ENDED' % self._testID)
