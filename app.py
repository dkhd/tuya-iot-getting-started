from dotenv import load_dotenv
load_dotenv()

import os

from tuya_iot import TuyaOpenAPI, tuya_logger

ENDPOINT = os.environ.get('ENDPOINT')
ACCESS_ID = os.environ.get('ACCESS_ID')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
DEVICE_ID = os.environ.get('DEVICE_ID')

# Initialization of tuya openapi
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.login(USERNAME, PASSWORD)

import logging
tuya_logger.setLevel(logging.DEBUG)

flag = True
while True:
    input('Hit Enter to toggle light switch.')
    flag = not flag
    commands = {'commands': [{'code':'switch_led','value': flag}]}
    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)