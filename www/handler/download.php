<?php
	function downfile(){
		$filename = $_SERVER['DOCUMENT_ROOT'].'/files/downloadfile.dld';

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
	downfile();
?>