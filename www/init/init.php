<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en",lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=utf8">
	<link rel="stylesheet" href="includes/style.css" type="text/css" media="screen" />
	<title>Init Databases</title>
</head>
<body>
	<?php # this file only superadimin can excute

		function initDatabase($dbconf,$initfile){
			/*
				pramas : $dbconf $initfile
				return TRUE / FALSE
			*/
			//check file
			printf("<p>Check config</p>\n");
			try{
				$db_host = $dbconf['db_host'];
				$db_port = $dbconf['db_port'];
				$db_name = $dbconf['db_name'];
				$db_user = $dbconf['db_user'];
				$db_pwd  = $dbconf['db_pwd'];
				if (isset($db_host) &&  isset($db_port) && isset($db_name) && isset($db_user) && isset($db_pwd)){

				}else{
					throw new Exception("Db config error ! Check db config !");
				}
			}catch(Exception $e){
				printf("<p>Config Args Error : %s </p>\n",$e->message());
				return FALSE;
			}
			printf("<p> Config SUCCESS! </p> \n");
			printf("<p>Try to open %s ...</p>\n",$initfile);
			try{
				$file = fopen($initfile, "r");
				$create_sql_array =array();
				$sql_line = '';
				while(!feof($file)){
					$line = fgets($file);
					$has =stripos($line,"//");
					$comments1 = stripos($line,'--');
					$comments2 = stripos($line,'/*');
					if ($comments1 == FALSE && $comments2 == FALSE){
						if($has === FALSE){
							$sql_line =$sql_line . $line;
						}else{
							$create_sql_array[] = $sql_line;
							$sql_line ='';
						}
					}
				}
			}catch(Exception $e){
				printf("<p>Open %s fieled : %s</p>\n",$initfile,$e->message());
				fclose($file);
				return FALSE;
			}finally{
				fclose($file);
			}
			printf("<p>Read %s over , SUCCESS ! </p>\n",$initfile);
			//check database
			printf("<p>Try to init Database  %s....</p>\n",$db_name);
			try{
				//create connect
				$mysql_conn = @mysqli_connect($db_host,$db_user,$db_pwd,"",$db_port) or die ('Could not connect to MYSQL: '.mysqli_connect_error());

				//set connect charset
				mysqli_set_charset($mysql_conn,'utf8');

				//init db
				$sql = "CREATE DATABASE IF NOT EXISTS ".$db_name;
				$result = $mysql_conn -> query($sql);

				#select db
				mysqli_select_db($mysql_conn,$db_name);

				foreach($create_sql_array as $sql_state){
					$result = $mysql_conn ->multi_query($sql_state);
					if ($result === TRUE){
						#echo "<p> EXCUTE SUCCESS : $sql_state </p>\n";
					}else{
						echo "<p> EXCUTE FILDED :  $sql_state </p>\n";
						printf("<p> ERROR  %s</p>\n",$mysql_conn ->error);
					}
					if ($mysql_conn ->more_results()){
						$mysql_conn ->next_result();
					}
				}
			}catch(Exception $e){
				printf("init DB fieled : %s",$e->message());
				mysqli_close($mysql_conn);
				return FASLE;
			}finally{
				
			}
			#init information show
			#select `name` from mysql.proc where db = "market_proc" and type = "PROCEDURE"; get all create procedure
			#show tables;

			$check_table_sql = "show tables;";
			$result = $mysql_conn -> query($check_table_sql);
			printf("<p>Ceate %s information</p>\n",$db_name);
			printf('<table border ="1">');
			printf("<tr><th>Tables</th></tr>");
			while($row = $result ->fetch_row()){
				printf("<tr><td>%s</td><tr>",$row[0]);
			}
			printf("</table>");
			printf("<p/>");
			mysqli_free_result($result);
			$check_proc_sql ="select `name` from mysql.proc where db = \"$db_name\" and type = \"PROCEDURE\";";
			$result1 = $mysql_conn -> query($check_proc_sql);
			printf('<table border ="1">');
			printf("<tr><th>Procedures</th></tr>");
			while($row1= $result1 ->fetch_row()){
				printf("<tr><td>%s</td></tr>",$row1[0]);
			}
			printf("</table>");
			mysqli_free_result($result1);
			mysqli_close($mysql_conn);
			printf("<p>Init Database %s SUCCESS !</p>",$db_name);
			return TRUE;
		}

		#file config
		$proc_file = 'initproc.sql';
		$proc_db_config['db_host'] = '127.0.0.1';
		$proc_db_config['db_port'] = 3306;
		$proc_db_config['db_name'] = 'market_proc';
		$proc_db_config['db_user'] = 'root';
		$proc_db_config['db_pwd']  = 'root';

		if(initDatabase($proc_db_config,$proc_file) === FALSE){
			printf("<p>Init %s failed ! Check init config ...</p> \n",$proc_db_config['db_name']);
		}

		$log_file = 'initlog.sql';
		$log_db_config['db_host'] = '127.0.0.1';
		$log_db_config['db_port'] = 3306;
		$log_db_config['db_name'] = 'market_log';
		$log_db_config['db_user'] = 'root';
		$log_db_config['db_pwd']  = 'root';

		if(initDatabase($log_db_config,$log_file) === FALSE){
			printf("<p>Init %s failed ! Check init config ...</p> \n",$log_db_config['db_name']);
		}
	?>
</body>
</html>