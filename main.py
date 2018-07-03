from Adafruit_SHT31 import *
import time
import logging
import glob

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient, AWSIoTMQTTShadowClient
from config.settings import IOT_CLIENT_ID, IOT_ENDPOINT

logging.basicConfig(level=logging.INFO)

ca_path = glob.glob('config/*Authority*.pem')
key_path = glob.glob('config/*private.pem.key')
cert_path = glob.glob('config/*certificate.pem.crt')


def build_shadow_client():
    myShadowClient = AWSIoTMQTTShadowClient(IOT_CLIENT_ID)
    # For Websocket connection
    # myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
    # Configurations
    # For TLS mutual authentication
    myShadowClient.configureEndpoint(IOT_ENDPOINT, 8883)
    # For Websocket
    # myShadowClient.configureEndpoint("YOUR.ENDPOINT", 443)
    # For TLS mutual authentication with TLS ALPN extension
    # myShadowClient.configureEndpoint("YOUR.ENDPOINT", 443)
    myShadowClient.configureCredentials(ca_path[0], key_path[0], cert_path[0])
    # For Websocket, we only need to configure the root CA
    # myShadowClient.configureCredentials("YOUR/ROOT/CA/PATH")
    myShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myShadowClient.configureMQTTOperationTimeout(5)  # 5 sec
    return myShadowClient


def build_mqtt_client():
    # For certificate based connection
    myMQTTClient = AWSIoTMQTTClient(IOT_CLIENT_ID)
    # For Websocket connection
    # myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
    # Configurations
    # For TLS mutual authentication
    myMQTTClient.configureEndpoint(IOT_ENDPOINT, 8883)
    # For Websocket
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    # For TLS mutual authentication with TLS ALPN extension
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    myMQTTClient.configureCredentials(ca_path[0], key_path[0], cert_path[0])
    # For Websocket, we only need to configure the root CA
    # myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
    myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
    return myMQTTClient


def main():
    try:
        sensor = SHT31(address=0x44)
    except:
        logging.warning('Temperature and humidity sensor cannot be loaded')
        sensor = None

    if not ca_path or not key_path or not cert_path:
        logging.warning('Need CA, private key, and certificate file located in config/')
        iot_client = None
    else:
        logging.info('Building shadow client.')
        iot_client = build_shadow_client()

    if iot_client:
        logging.info('Connecting to IoT')
        iot_client.connect()
        logging.info('Connected to IoT!')
    else:
        logging.warning('Unable to connect to IoT')

    while True:
        if sensor:
            degrees = sensor.read_temperature()
            humidity = sensor.read_humidity()
            print('Temp             = {0:0.3f} deg C'.format(degrees))
            print('Humidity         = {0:0.2f} %'.format(humidity))
        time.sleep(5)


if __name__ == '__main__':
    main()
