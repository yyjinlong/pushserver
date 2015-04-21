1） pyOpenSSl 使用pip安装报错(ubuntu)：

    ```
    distutils.errors.DistutilsError: Setup script exited with error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

    解决办法：

        sudo apt-get install libffi-dev
        sudo apt-get install libssl-dev
        sudo apt-get install python-dev
    ```


2）运行apns模块，发送推送消息时，报错：

    ```
    OpenSSL.SSL.Error: [('SSL routines', 'SSL3_READ_BYTES', 'sslv3 alert handshake failure')]

    This error is due to the recent OpenSSL SSL v3 vulnerability known as Poodle.
    Apple (and many others) have disabled SSL v3 but APNSWrapper explicitly uses SSL v3.

    进入下载的apns-client-0.2.1的apns安装包里：
    ➜ backends git:(master) ✗ pwd
    /home/jinlong/github/pushserver/apns_pusher/apns-client-0.2.1/apnsclient/backends

    ➜  backends git:(master) ✗ vim stdio.py
    # NOTE: apple disable SSLV3
    42 # context = OpenSSL.SSL.Context(OpenSSL.SSL.SSLv3_METHOD)
    43 context = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_METHOD)

    fixed by replacing line 41 in backends/stdio.py withcontext = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_METHOD)

    之后，重写编译及安装apnsclient模块：
    ➜ apns-client-0.2.1 git:(master) ✗ pwd
    /home/jinlong/github/pushserver/apns_pusher/apns-client-0.2.1
    ➜ apns-client-0.2.1 git:(master) ✗
    ➜ apns-client-0.2.1 git:(master) ✗ ls
    apnsclient apns_client.egg-info build CHANGELOG dist LICENSE MANIFEST.in PKG-INFO README.rst setup.cfg setup.py test
    ➜ apns-client-0.2.1 git:(master) ✗
    ➜ apns-client-0.2.1 git:(master) ✗ sudo python setup.py build
    ➜ apns-client-0.2.1 git:(master) ✗ sudo python setup.py install
    ```

