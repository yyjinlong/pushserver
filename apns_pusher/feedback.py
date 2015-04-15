#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: jinlong.yang
#

from apnsclient import (
    Session,
    APNs
)
from pprint import pprint

session = Session()
conn =session.new_connection("feedback_sandbox", cert_file="apns.pem", passphrase="1234")

service = APNs(conn)
pprint(vars(service))

try:
    # on any IO failure after successfull connection this generator
    # will simply stop iterating. you will pick the rest of the tokens
    # during next feedback session.
    # feedback的接口取到的是上次推送的过程中出现的已卸载应用的设备token，而且获取一次之后就会清空
    for token, when in service.feedback():
        # every time a devices sends you a token, you should store
        # {token: given_token, last_update: datetime.datetime.now()})
        print token
        print when

        # the token wasn't updated after the failure has
        # been reported, so the token is invalid and you should
        # stop sending messages to it.

except Exception as _ex:
    print "connect to APNs failed, err: %s" %str(_ex)
