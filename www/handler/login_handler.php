<?php
function checkUserLogin($uname,$pwd,$flag){
	if ($uname === "superadmin" && $pwd === "superadmin"){
		echo "<p>Welcome superadmin !<p/>\n";
	}
	elseif($uname ==="aaaaa" && $pwd ="aaaaa"){
		echo "<p>Welcome member  !<p/>\n";
	}else{
		echo "<p class ='error'>login failed !<p/>\n";
	}
}
	if($_SERVER['REQUEST_METHOD'] == 'POST'){
		if(isset($_POST['uname'],$_POST['pwd'],$_POST['flag'])){
			$uname = $_POST['uname'];
			$pwd = $_POST['pwd'];
			$flag = $_POST['flag'];
			echo "<p>Uname : $uname </p>\n";
			echo "<p>Pwd :$pwd</p>\n";
			echo "<p>Flag: $flag</p>\n";
			checkUserLogin($uname,$pwd,$flag);
		}
	}else{

	}
?>