import os
from jinja2 import Environment, FileSystemLoader
from framework.utils.utils import OVC_BaseTest
from testconfig import config
import uuid
import logging
import time
import unittest

# this should inherit from zeroos (zos) class too


class constructor(unittest.TestCase):

    version = config['main']['version']

    # this pass for templatepath should be removed
    def __init__(self, *args, **kwargs):
        super(constructor, self).__init__(*args, **kwargs)
        templatespath='./framework/utils/templates'
        if templatespath:
            self.j2_env = Environment(loader=FileSystemLoader(searchpath=templatespath), trim_blocks=True)
            self.j2_env.globals.update(random_string=self.random_string)

    def Setup(self):
        self._testID = self._testMethodName
        self._startTime = time.time()
        self._logger = logging.LoggerAdapter(logging.getLogger('openvcloud_testsuite'),
                                             {'testid': self.shortDescription() or self._testID})

    def random_string(self):
        return str(uuid.uuid4())[0:8]

    # this is hardcoded .. need to be changed later
    def execute_blueprint(self, bp_yaml):
        os.system('echo "%s" >> /root/blueprints/bp.yaml' % bp_yaml)
        os.system('zrobot blueprint execute /root/blueprints/bp.yaml')

    def create_blueprint(self, yaml, **kwargs):
        """
        yaml file that is used for blueprint creation
        """
        kwargs['version'] = constructor.version
        blueprint = self.j2_env.get_template('base.yaml').render(services=yaml,
                                                                 actions='actions.yaml',
                                                                 **kwargs)
        return blueprint
