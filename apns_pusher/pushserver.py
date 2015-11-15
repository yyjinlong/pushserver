#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

from apnsclient import (
        Session,
        Message,
        APNs
)
from pprint import pprint

# device token and private key's passwd
deviceToken = '097271a3744d951fe233729b649b0d5bcdfbf7e0c8c10e11fa99d02e5cfa87ac';
invalid_deviceToken = '097271a3744d951fe233729b649b0d5bcdfbf7e0c8c10e11fa99d02e5cfa87ed';
passphrase = '1234';

# 使用session对象来创建一个连接池
session = Session()
conn = session.get_connection("push_sandbox", cert_file="apns.pem", passphrase=passphrase)

# 发送推送和得到反馈
tokenList = []
tokenList.append(deviceToken)
#tokenList.append(invalid_deviceToken)
msg = Message(tokenList, alert="use python send", badge=10)

# send message
service = APNs(conn)
res = service.send(msg)

pprint(vars(res))
print res.message.__dict__
