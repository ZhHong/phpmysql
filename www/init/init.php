<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en",lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=utf8">
	<title>Init Mysql</title>
</head>
<body>
	<?php
		$filename = "initproc.sql";
		$file = fopen($filename,"r");
		$create_sql_array = array();
		$sql_line ="";
		if ($file){
			while (!feof($file)) {
				$line = fgets($file);
				//if not have // end the of the function
				$has = stripos($line,"//");
				if ($has === FALSE){
					$sql_line = $sql_line.$line;
				}else{
					$create_sql_array[] = $sql_line;
					$sql_line ="";
				}
			}
		}else{
			echo "open $filename failed !!";
		}
		
		foreach($create_sql_array as $sql_state){
			echo "<p>$sql_state </p>\n\n";
		}
	?>
</body>
</html>