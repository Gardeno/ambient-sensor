from Adafruit_SHT31 import *
from common import build_shadow_client
import time
import logging
import json

from config.settings import IOT_CLIENT_ID, IOT_SHADOW_TIMEOUT_SECONDS

logging.basicConfig(level=logging.INFO)


def shadow_callback(payload, responseStatus, token):
    logging.info('Received shadow update response with status {} and payload {}'.format(responseStatus, payload))


def main():
    try:
        sensor = SHT31(address=0x44)
    except:
        logging.warning('Temperature and humidity sensor cannot be loaded')
        sensor = None

    shadow_client = build_shadow_client()

    if shadow_client:
        logging.debug('Connecting to IoT')
        shadow_client.connect()
        logging.debug('Connected to IoT!')
        logging.debug('Creating shadow handler')
        shadow_client_shadow = shadow_client.createShadowHandlerWithName(IOT_CLIENT_ID, True)
        logging.debug('Created shadow handler!')
    else:
        logging.warning('Unable to connect to IoT')

    while True:
        if sensor:
            degrees = sensor.read_temperature()
            humidity = sensor.read_humidity()
            print('Temp             = {0:0.3f} deg C'.format(degrees))
            print('Humidity         = {0:0.2f} %'.format(humidity))
            if shadow_client:
                shadow_client_shadow.shadowUpdate(json.dumps({
                    'state': {
                        'reported': {
                            'temperature': degrees,
                            'humidity': humidity,
                        }
                    }
                }), shadow_callback, IOT_SHADOW_TIMEOUT_SECONDS)
        time.sleep(5)


if __name__ == '__main__':
    main()
