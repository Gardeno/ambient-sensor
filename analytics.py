#!/usr/bin/python

from common import build_shadow_client
import logging

from config.settings import IOT_CLIENT_ID, IOT_SHADOW_TIMEOUT_SECONDS

logging.basicConfig(level=logging.INFO)


def shadow_callback(payload, responseStatus, token):
    logging.info('Received shadow update response with status {} and payload {}'.format(responseStatus, payload))


def main():
    shadow_client = build_shadow_client()
    if not shadow_client:
        logging.error('Unable to build shadow client')
        return

    shadow_client.connect()
    # shadow_client_shadow = shadow_client.createShadowHandlerWithName(IOT_CLIENT_ID, False)

    # shadow_client_shadow.shadowGet(shadow_callback, IOT_SHADOW_TIMEOUT_SECONDS)


if __name__ == '__main__':
    main()
