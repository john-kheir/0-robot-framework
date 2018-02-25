import logging
import os
from testconfig import config
from js9 import j

# Initiate testsuite logger
logger = logging.getLogger('openvcloud_testsuite')
if not os.path.exists('logs/openvcloud_testsuite.log'):
    os.mkdir('logs')
handler = logging.FileHandler('logs/openvcloud_testsuite.log')
formatter = logging.Formatter('%(asctime)s [%(testid)s] [%(levelname)s] %(message)s',
                              '%d-%m-%Y %H:%M:%S %Z')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# configure itsyouonline instance
app_id = config['main']['app_id']
secret = config['main']['secret']
data = {
    "baseurl": "https://itsyouonline/api",
    "application_id_": app_id,
    "secret_": secret
}
j.clients.itsyouonline.get(instance="main", data=data)
