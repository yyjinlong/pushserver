#mosquitto install and use
--------------------------
author: jinlong.yang

1) 源码安装

    # wget  http://mosquitto.org/files/source/mosquitto-1.4.2.tar.gz 
    # tar zxfv mosquitto-1.4.2.tar.gz
    # cd mosquitto-1.4.2
    # sudo make
    # sudo make install

2) 遇到的报错

    (1) fatal error uuid/uuid.h no such file or directory
    解决办法：
    sudo apt-get install uuid-dev

    (2) Error: Invalid user 'mosquitto'.
    解决办法：
    1）修改mosquitto.conf配置文件，将 user mosquitto解注释
    2）添加mosquitto用户：# useradd mosquitto

    (3) error while loading shared libraries: libmosquitto.so.1: cannot open shared object file: No such file or directory
    解决办法：
    # 创建链接
    sudo ln -s /usr/local/lib/libmosquitto.so.1 /usr/lib/libmosquitto.so.1
    # 更新动态链接库
    sudo ldconfig

3) 配置&运行

    拷贝配置文件
    # cd /etc/mosquitto
    # cp mosquitto.conf.exmaple mosquitto.conf

    运行
    # mosquitto -c /etc/mosquitto/mosquitto.conf -d

    接收：
    # mosquitto_sub -v -t levis

    发送：
    # mosquitto_pub -h localhost -t levis -m "hello world"

4) mosquitto 的python client:

    m_sub.py ---> mosquitto_sub -v -t levis
    m_pub.py ---> mosquitto_pub -h localhost -t levis -m "hello world"

5) 配置android客户端来连接mosquitto进行消息推送

    AndroidMqttDemo ： android mqtt demo 列子
    修改src/com/tokudu/demo/PushService.java:
    MQTT_HOST修改为你的mosquitto的地址
    MQTTCOnnection函数里的initTopic  修改为“levis"
    之后运行,并启动Start Push service服务

    终端运行：
    $ mosquitto_pub -h localhost -t levis -m "hello world"

    或者直接运行：
    $ python m_pub.py

