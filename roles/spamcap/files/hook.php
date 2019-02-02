#!/usr/bin/php
<?php
$file = fopen("/tmp/postfixtest", "a");
fwrite($file, "New email send attempt at ".date("Y-m-d H:i:s")."\n");

// read from stdin
$fd = fopen("php://stdin", "r");
$email = "";
while (!feof($fd)) {
    $line = fread($fd, 1024);
    $email .= $line;
}
fclose($fd);

fwrite($file, $email);
fclose($file);

?>