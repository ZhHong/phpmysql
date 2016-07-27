<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en",lang="en">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=utf8">
	<title>HTML Form</title>
	<style type="text/css" tittle = "text/css" media = "all">
		label {
			font-weight: :bold;
			color: #300ACC;
		}
	</style>
</head>
<body>
	
	<form accept-charset="utf8" action="handler_form.php" method="post">
		<fieldset><lengend>Enter your information in form below: </lengend>
		<p><label>Name:<input type = "text" name = "name" size="20" maxlength="40"/></label></p>
		<p><label>Email Address:<input type ="text" name="email" size="40" maxlength ="60"/></label></p>
		<p><label for ="gender">Gender:</label><input type ="radio" name="gender" value ="M"/> Male <input type ="radio" name="gender" value ="F" />Female </p>
		<p><label>Age:
			<select name="age">
				<option value="0-29">Under 30 </option>
				<option value="30-60">Between 30 and 60 </option>
				<option value="60+">Over 60 </option>
			</select>
		</label></p>
		<p><label>
			Coments:<textarea name ="comments" rows ="3" cols="40"></textarea>
		</label></p>
		</fieldset>
		<p align="center"><input type="submit" name="submit" value="Submit my Information" /></p>
	</form>
</body>
</html>