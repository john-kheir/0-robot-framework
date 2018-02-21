from jinja2 import Environment, FileSystemLoader
from framework.utils.utils import OVC_BaseTest


# this should inherit from zeroos (zos) class too


class constructor(OVC_BaseTest):

    # put elements that are the same for all objects
    # static_elem = 123
    ## this pass for templatepath should be removed
    def __init__(self, *args, **kwargs):
        # object elements
        templatespath='./framework/utils/templates'
        if templatespath:
            self.j2_env = Environment(loader=FileSystemLoader(searchpath=templatespath), trim_blocks=True)
            self.j2_env.globals.update(random_string=self.random_string)
        super(constructor, self).__init__(*args, **kwargs)

    def random_string(self):
        import uuid
        return str(uuid.uuid4())[0:8]

    def create_blueprint(self, yaml, **kwargs):
        """
        yaml file that is used for blueprint creation
        """
        text = self.j2_env.get_template('base.yaml').render(services=yaml,
                                                            actions='actions.yaml',
                                                            **kwargs)
        print(text)
        return text
