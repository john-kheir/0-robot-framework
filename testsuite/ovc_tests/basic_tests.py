import time
from zerorobot.dsl.ZeroRobotAPI import ZeroRobotAPI
from framework.utils.utils import OVC_BaseTest
from collections import OrderedDict


class BasicTests(OVC_BaseTest):
    # we can put this on __init__.py
    def __init__(self, *args, **kwargs):
        super(BasicTests, self).__init__(*args, **kwargs)

    def setUp(self):
        super(BasicTests, self).setUp()
        self.acc1 = self.random_string()
        self.cs1 = self.random_string()
        self.accounts = [{self.acc1: {}}]
        self.cloudspaces = [{self.cs1: {}}]

    def test001_trial(self):
        """ ZRT-OVC-001
        *Test case for ...*

        **Test Scenario:**

        #. Create an account and 2 cloudspaces, should succeed.
        #. check that the cloudspaces have been created.
        """
        self.log('%s STARTED' % self._testID)

        self.cs2 = self.random_string()
        self.vdcuser = self.random_string()
        self.vdcusers.extend([{self.vdcuser: {'provider': 'itsyouonline', 'email': 'abdelmab@greenitglobe.com'}}])
        self.cloudspaces.extend([{self.cs2: {'users': OrderedDict([('name', self.vdcuser), ('accesstype', 'CXDRAU')])}}])
        self.temp_actions = {'account': ['install'], 'vdcuser': ['install'], 'vdc': ['install']}

        self.log('Create 1 account and 2 cloudspaces, should succeed')
        self.create_cs(vdcusers=self.vdcusers, accounts=self.accounts,
                       cloudspaces=self.cloudspaces, temp_actions=self.temp_actions)

        # wait till blueprint is executed
        self.wait_for_service_action_status(self.cs2)

        self.log('check that the cloudspaces have been created')
        self.assertTrue(self.get_cloudspace(self.cs1))
        self.assertTrue(self.get_cloudspace(self.cs2))

        self.log('%s ENDED' % self._testID)

    def tearDown(self):
        self.delete_services()
        self.temp_actions = {'account': ['uninstall']}
        self.create_account(vdcusers=self.vdcusers, accounts=self.accounts,
                            temp_actions=self.temp_actions)
        self.delete_services()
