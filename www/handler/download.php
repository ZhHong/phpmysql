<?php
	function downfile($name){
		$filename = $_SERVER['DOCUMENT_ROOT'].'/files/'.$name;
		#check file
		if(file_exists($filename) === false){
			echo "file:".$name."not on the server!";
		}
		header('Content-Description: File Transfer');
		header('Content-Type: application/octet-stream');
		header('Content-Disposition: attachment; filename='.basename($filename));
		header('Content-Transfer-Encoding: binary');
		header('Expires: 0');
		header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
		header('Pragma: public');
		header('Content-Length: ' . filesize($filename));
		readfile($filename);
	}
?>