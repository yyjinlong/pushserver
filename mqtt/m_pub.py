#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

import paho.mqtt.publish as publish

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_SUBSCRIBE_THEME = "levis"


if __name__ == '__main__':
    test_msg = u"hello mosquitto server...."

    publish.single(MQTT_SUBSCRIBE_THEME,
            test_msg,
            hostname=MQTT_BROKER,
            port=MQTT_PORT)
