import os
from jinja2 import Environment, FileSystemLoader
from zerorobot.dsl.ZeroRobotAPI import ZeroRobotAPI
import uuid
import logging
import time
import unittest
from testconfig import config


class constructor(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(constructor, self).__init__(*args, **kwargs)
        templatespath = './framework/utils/templates'
        self.j2_env = Environment(loader=FileSystemLoader(searchpath=templatespath), trim_blocks=True)
        self.j2_env.globals.update(random_string=self.random_string)
        self.j2_env.globals.update(config_params=self.config_params)
        self.api = ZeroRobotAPI()

    def setUp(self):
        self._testID = self._testMethodName
        self._startTime = time.time()
        self._logger = logging.LoggerAdapter(logging.getLogger('openvcloud_testsuite'),
                                             {'testid': self.shortDescription() or self._testID})

    def random_string(self):
        return str(uuid.uuid4())[0:8]

    def config_params(self, param):
        return config['main'][param]

    def log(self, msg):
        self._logger.info(msg)

    # this is hardcoded .. need to be changed later
    def execute_blueprint(self, bp_yaml):
        os.system('echo "%s" >> /root/bp.yaml' % bp_yaml)
        os.system('zrobot blueprint execute /root/bp.yaml')
        os.system('rm /root/bp.yaml')

    def delete_services(self):
        for serviceguid in self.api.services.guids.keys():
            os.system('zrobot service delete %s' % serviceguid)

    def create_blueprint(self, yaml, **kwargs):
        """
        yaml file that is used for blueprint creation
        """
        blueprint = self.j2_env.get_template('base.yaml').render(services=yaml,
                                                                 actions='actions.yaml',
                                                                 **kwargs)
        return blueprint

    def wait_for_service_action_status(self, servicename, action='install',
                                       status='ok', timeout=200):
        service = self.api.services.names[servicename]
        for i in range(timeout):
            time.sleep(1)
            state = service.state.categories
            if state:
                self.assertEqual(service.state.categories['actions'][action], status)
        #self.assertTrue(state, "No state has been found")
        #self.assertTrue(False, state)
