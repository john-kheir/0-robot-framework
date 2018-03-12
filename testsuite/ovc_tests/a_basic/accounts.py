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
        self.temp_actions = {'account': ['install'], 'vdcuser': ['install']}

    def test001_create_account_with_wrong_params(self):
        """ ZRT-OVC-001
        *Test case for creating account with different or missing parameters*

        **Test Scenario:**

        #. Create an account without providing openvcloud parameter, should fail.
        #. Create an account with providing non existing parameter, should fail.
        """
        self.log('%s STARTED' % self._testID)

        self.accounts = [{self.acc1: {}}]

        self.log('Create an account without providing openvcloud parameter, should fail')
        res = self.create_account(openvcloud=self.openvcloud, vdcusers=self.vdcusers,
                                  accounts=self.accounts, temp_actions=self.temp_actions)
        self.assertEqual(res, 'openvcloud is mandatory')

        self.log('Create an account with providing non existing parameter, should fail')

        self.log('%s ENDED' % self._testID)

    def test002_create_account_with correct_params(self):
        """ ZRT-OVC-002
        *Test case for creating account with correct parameters*

        **Test Scenario:**

        #. Create an account, should succeed.
        #. Check if the account parameters are reflected correctly on OVC.
        #. Update some parameters and make sure it is updated.
        """
        self.log('%s STARTED' % self._testID)

        CU_D = 2
        CU_C = 2
        CU_I = 2
        CU_M = 2
        self.accounts = [{self.acc1: {'openvcloud': self.openvcloud, 'maxMemoryCapacity': CU_M,
                                      'maxCPUCapacity': CU_C, 'maxDiskCapacity': CU_D, 'maxNumPublicIP', CU_I,
                                      'users': 2}}]

        self.log('Create an account, should succeed')
        res = self.create_account(openvcloud=self.openvcloud, vdcusers=self.vdcusers,
                                  accounts=self.accounts, temp_actions=self.temp_actions)
        self.assertTrue(res, True)

        self.log('Check if the account parameters are reflected correctly on OVC')
        account = self.get_account(self.acc1)
        self.assertTrue(account)
        self.assertEqual(account['resourceLimits']['CU_D'], CU_D)
        self.assertEqual(account['resourceLimits']['CU_C'], CU_C)
        self.assertEqual(account['resourceLimits']['CU_I'], CU_I)
        self.assertEqual(account['resourceLimits']['CU_M'], CU_M)

        self.log('Update some parameters and make sure it is updated')

        self.log('%s ENDED' % self._testID)

    def tearDown(self):
        #check if there is a service of kind account
        #self.temp_actions = {'account': ['uninstall']}
        #self.create_account(openvcloud=self.openvcloud, vdcusers=self.vdcusers,
        #                    accounts=self.accounts, temp_actions=self.temp_actions)
        self.delete_services()
