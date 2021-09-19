from dotenv import load_dotenv
load_dotenv()

import os

from tuya_iot import TuyaOpenAPI, TuyaOpenMQ, tuya_logger

ENDPOINT = os.environ.get('ENDPOINT')
ACCESS_ID = os.environ.get('ACCESS_ID')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
DEVICE_ID = os.environ.get('DEVICE_ID')  # Actual Powered By Tuya Device ID

import logging
tuya_logger.setLevel(logging.DEBUG)

# Initialization of tuya openapi    
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.login(USERNAME, PASSWORD)

# Receive device message
def on_message(msg):
    print("on_message: %s"% msg)

openmq = TuyaOpenMQ(openapi)
openmq.start()
openmq.add_message_listener(on_message)