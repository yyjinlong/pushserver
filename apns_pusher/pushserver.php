<?php
/* ini_set("display_errors", "On");
error_reporting(E_ALL | E_STRICT); */
 
// Put your device token here (without spaces):
$deviceToken = '097271a3744d951fe233729b649b0d5bcdfbf7e0c8c10e11fa99d02e5cfa87ac';
// Put your private key's passwd here:
$passphrase = '1234';
 
// Put your alert message here:
$message = 'Welcome to www.elesos.com';
 
/*
 * stream_context_create — 创建并返回资源流上下文
 * stream_context_set_option — 对资源流、数据包或者上下文设置参数
 * stream_socket_client — Open Internet or Unix domain socket connection
 */
$ctx = stream_context_create();
stream_context_set_option($ctx, 'ssl', 'local_cert', 'apns.pem');
stream_context_set_option($ctx, 'ssl', 'passphrase', $passphrase);
 
// Open a connection to the APNS server
$fp = stream_socket_client(
    'ssl://gateway.sandbox.push.apple.com:2195', $err,
    $errstr, 60, STREAM_CLIENT_CONNECT|STREAM_CLIENT_PERSISTENT, $ctx);
 
if (!$fp)
    exit("Failed to connect: $err $errstr" . PHP_EOL);
 
echo 'Connected to APNS' . PHP_EOL;
 
// Create the payload body
$body['aps'] = array(
    'alert' => $message,
    'badge'=>1,
    'sound' => 'default'
    );
 
// Encode the payload as JSON
$payload = json_encode($body);
 
// Build the binary notification
$msg = chr(0) . pack('n', 32) . pack('H*', $deviceToken) . pack('n', strlen($payload)) . $payload;
 
// Send it to the server
$result = fwrite($fp, $msg, strlen($msg));
 
if (!$result)
    echo 'Message not delivered' . PHP_EOL;
else
    echo 'Message successfully delivered' . PHP_EOL;
 
// Close the connection to the server
fclose($fp);

