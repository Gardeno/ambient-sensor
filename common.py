import glob
import logging
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
from config.settings import IOT_CLIENT_ID, IOT_ENDPOINT
import os

BASE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def build_shadow_client():
    certificate_authority = glob.glob(os.path.join(BASE_DIRECTORY, 'config', '*Authority*.pem'))
    private_key = glob.glob(os.path.join(BASE_DIRECTORY, 'config', '*private.pem.key'))
    certificate = glob.glob(os.path.join(BASE_DIRECTORY, 'config', '*certificate.pem.crt'))
    if not certificate_authority or not private_key or not certificate:
        logging.warning('Need CA, private key, and certificate file located in config/')
        return None
    shadow_client = AWSIoTMQTTShadowClient(IOT_CLIENT_ID)
    shadow_client.configureEndpoint(IOT_ENDPOINT, 8883)
    shadow_client.configureCredentials(certificate_authority[0], private_key[0], certificate[0])
    shadow_client.configureConnectDisconnectTimeout(10)
    shadow_client.configureMQTTOperationTimeout(5)
    return shadow_client
