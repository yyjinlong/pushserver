pushserver
----------
author: jinlong.yang

1) pushserver.plist: 内网ipa下载，使用itms-service协议

    ios 7.1 后，规定plist必须使用https访问。所以itms-service使用的plist必须是https的,
    github是https，所以可以使用github作为练习使用。

2) pushserver.php: pushserver php 版本后端

    php版本的推送后端

3) pushserver.py: pushserver python 版本后端

    python版本的推送后端，包括feedback service

4) feedback.py: pushserver 的定时任务

    python版本feedback service, 用于获取失效的token

5) push_ios: pushserver ios native 版本app

    ios native 版本推送demo

6) android mqtt demo

    android mqtt demo -> AndroidMqttDemo

