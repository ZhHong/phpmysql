<?php
	$host ="127.0.0.1";
	$port ="8080";

	$socket = socket_create(AF_INET, SOKET_STREAM, SOL_TCP);

	if ($socket === false){
		echo " create socket failed. reason:".socket_strerror(socket_last_error())."\n";
	}else{
		echo " create socket ok ."
	}
	$result = socket_connect($socket, $host,$port);
	if ($result === false){
		echo "socket_connect failed. reason:".socket_strerror(socket_last_error($socket))."\n";
	}else{
		echo " connect to server :".$host.":".$port."\n";
	}
	$msg = socket_read($socket, 8192);

	echo "read msg :".$msg."\n";
?>