import glob
import logging
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
from config.settings import IOT_CLIENT_ID, IOT_ENDPOINT


def build_shadow_client():
    ca_path = glob.glob('config/*Authority*.pem')
    key_path = glob.glob('config/*private.pem.key')
    cert_path = glob.glob('config/*certificate.pem.crt')
    if not ca_path or not key_path or not cert_path:
        logging.warning('Need CA, private key, and certificate file located in config/')
        return None
    shadow_client = AWSIoTMQTTShadowClient(IOT_CLIENT_ID)
    shadow_client.configureEndpoint(IOT_ENDPOINT, 8883)
    shadow_client.configureCredentials(ca_path[0], key_path[0], cert_path[0])
    shadow_client.configureConnectDisconnectTimeout(10)
    shadow_client.configureMQTTOperationTimeout(5)
    return shadow_client
