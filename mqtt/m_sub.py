#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_SUBSCRIBE_THEME = "levis"
#在推送的时候，就是安卓的设备id
MQTT_CLIENT_ID = "45464748"


def on_connect(client, userdata, flags, rc):
    print "connect to mosquitto with result code: %s" % str(rc)
    client.subscribe(MQTT_SUBSCRIBE_THEME)

def on_message(client, userdata, msg):
    print "topic: %s, message: %s" %(msg.topic, msg.payload)


if __name__ == '__main__':
    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
    mqtt_client.loop_forever()

