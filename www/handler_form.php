<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en",lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=utf8">
	<title>Form Feedback</title>
	<style type="text/css" title="text/css" media ="all">
		.error{
			font-weight: bold;
			color: #C00;
		}
	</style>
</head>
<body>
	<?php #Script 2.2 - handler_form.php
	//recive form data
	// if (!empty($_REQUEST['name'])){
	// 	$name = $_REQUEST['name'];
	// }else{
	// 	$name = NULL;
	// 	echo '<p class="error">You forgot to enter your name !</p>';
	// }
	// if(!empty($_REQUEST['email'])){
	// 	$email = $_REQUEST['email'];
	// }else{
	// 	$email = NULL;
	// 	echo '<p class="error">You forgot to enter your email !</p>';
	// }
	// if(!empty($_REQUEST['comments'])){
	// 	$comments = $_REQUEST['comments'];
	// }else{
	// 	$comments =NULL;
	// 	echo '<p class="error">Your forgot to enter your comments !</p>';
	// }
	// /* not used
	// $_REQUEST['age']
	// $_REQUEST['gender']
	// $_REQUEST['submit']
	// */
	// if(isset($_REQUEST['gender'])){
	// 	$gender =$_REQUEST['gender'];
	// 	if($gender =="M"){
	// 		echo "<p><b>Good day,Sir !</b> </p>";
	// 	}elseif($gender == "F"){
	// 		echo "<p><b>Good day , Madam! </b></p>";
	// 	}else{
	// 		$gender = NULL;
	// 		echo '<p class="error">Gander should be either "M" or "F" !</p>';
	// 	}
	// }else{
	// 	$gender = NULL;
	// 	echo '<p class= "errpr">You forget to select your gender !</p>';
	// }
	
	// if ($name && $email &&$gender && $comments){
	// 	echo "<p>Thank you, <b>$name</b>, for the following comments:<br />
	// 	<tt>$comments</tt></p>
	// 	<p>We will reply to you at <i>$email</i>.</p>\n";
	// }else{
	// 	echo '<p class ="error"> Please go back and fill out the form again.</p>';
	// }
		if(!empty($_POST['name']) && !empty($_POST['email']) && ! empty($_POST['comments'])){
			echo "<p>Thank you, <b>{$_POST['name']}</b>, for the following comments:<br />
			<tt>{$_POST['comments']}</tt></p>
			<p>We will reply to you at <i>{$_POST['email']}</i>.</p>\n";
		}else{
			echo '<p class ="error"> Please go back and fill out the form again.</p>';
		}
	?>
</body>
</html>