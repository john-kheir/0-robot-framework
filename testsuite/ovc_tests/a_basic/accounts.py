import time
from zerorobot.dsl.ZeroRobotAPI import ZeroRobotAPI
from framework.utils.utils import OVC_BaseTest
from collections import OrderedDict


class accounts(OVC_BaseTest):
    def __init__(self, *args, **kwargs):
        super(accounts, self).__init__(*args, **kwargs)

    def setUp(self):
        super(accounts, self).setUp()
        self.acc1 = self.random_string()
        self.accounts = [{self.acc1: {'openvcloud': self.openvcloud}}]

    def test001_create_account_with_different_params(self):
        """ ZRT-OVC-001
        *Test case for creating account with different parameters*

        **Test Scenario:**

        #. Create an account without providing openvcloud parameter, should fail.
        #. Create an account with providing non existing parameter, should fail.
        """
        self.log('%s STARTED' % self._testID)

        self.vdcuser = self.random_string()
        self.accounts = [{self.acc1: {}}]
        self.temp_actions = {'account': ['install'], 'vdcuser': ['install']}

        self.log('Create an account without providing openvcloud parameter, should fail')
        res = self.create_cs(openvcloud=self.openvcloud, vdcusers=self.vdcusers,
                             accounts=self.accounts, temp_actions=self.temp_actions)
        self.assertEqual(res, 'openvcloud is mandatory')

        self.log('Create an account with providing non existing parameter, should fail')

        self.log('%s ENDED' % self._testID)

    def tearDown(self):
        #check if there is a service of kind account
        #self.temp_actions = {'account': ['uninstall']}
        #self.create_account(openvcloud=self.openvcloud, vdcusers=self.vdcusers,
        #                    accounts=self.accounts, temp_actions=self.temp_actions)
        self.delete_services()
