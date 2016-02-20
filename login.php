<?php
	function salt() {
		$chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[{}]\|<>.?/';
		$salt = "";
		$length = 30;

		for($i = 0; $i < $length; $i++){
			$salt .= substr(str_shuffle($chars), mt_rand(0, strlen($chars)), 1);
		}
		return $salt;
	}

	$userName =  $_POST['username'];
	$password = $_POST['password'];
	$number = $_POST['number'];
	$filePath1 = "/websites/secure/www/users.txt";
	$filePath2 = "/websites/secure/www/init1.txt";
	$filePath3 = "/websites/secure/www/index.json";
	if(file_exists($filePath1)) {
		if(filesize($filePath1) <= 1){
			//Register
			$fh2 = fopen($filePath2, 'r');
			$d = fread($fh2, filesize($filePath2));
			$data = explode(',', $d);
			$s1 = $data[1];
			$reg = $data[0];
			if($reg == hash("sha256", ($number . $s1), FALSE)){
				$fh = fopen($filePath1, 'w+');
				$s2 = salt();
				$u = hash("sha256", ($s1 . $userName. $s2), FALSE);
				$p = hash("sha256", ($s2 . $password . $s1), FALSE);
				fwrite($fh, $u . ',' . $p . ',' . $s1 . ',' . $s2);
				fflush($fh);
				fclose($fh);
				echo "0";
				//Set authentication to true
			}
			else{
				echo "1";
				//echo 'Incorrect registration value try again';
				//echo unlink($filePath1);
			}
		}
		else {
			//account set up as normal, check u and p
			$fh = fopen($filePath1, 'r');
			$k = fread($fh, filesize($filePath1));
			$data = explode (',', $k);
			fclose($fh);
			$u = $data[0];
			$p = $data[1];
			$s1 = $data[2];
			$s2 = $data[3];

			$hu1 = hash("sha256", ($s1 . $userName . $s2), FALSE);
			$hp1 = hash("sha256", ($s2 . $password . $s1), FALSE);

			if($u == $hu1 && $p == $hp1){
				echo "0";
				//echo "Login Successful";
				//$fh2 = fopen($filePath3, 'r');
				//$d = fread($fh2, filesize($filePath3));
				//echo $d ;
				$fh3 = fopen($filePath3, 'r');
				$d = fread($fh3, filesize($filePath3));
				echo $d ;
				fflush($fh3);
				fclose($fh3);
			}
			else{
				echo "1";
				//echo "Try again";
			}
		}
	}
	else {
		//no one is registered, create account
		$fh2 = fopen($filePath2, 'r');
		$d = fread($fh2, filesize($filePath2));
		fclose($fh2);

		$data =  explode(',', $d);
		$s1 = $data[1];
		$reg = $data[0];
		//$number = "123456789101112131415";
		/*$s = salt();
		$n = hash('sha256', ($number . $s), FALSE);
		$fh2 = fopen($filePath2, 'w+');
		fwrite($fh2, $n . ',' . $s);

		echo 'Success';
		exit();*/
		//echo $reg . '<br>';
		if($userName === 'user' && $password === 'password'){
			if($reg == hash("sha256", ($number . $s1), FALSE)){
				//Registration test page
				echo '0';
				//echo '<h1>Registered</h1> <br>
				//	<form action=login.php method="post">
				//	<table> <tr> <td>New Username</td><td><input type="text" name="username"size=30/></td></tr>
				//	<tr><td>New Password</td><td><input type="password" name="password" size=30></td></tr>
				//	<tr><td>Registration Number</td><td><input type="text" name="number" size=30></td></tr>
				//	<tr><td><input type="submit" value="Submit"/></td></tr>
				//	</table></form>';
				//touch the users.txt file
				$fh1 = fopen( $filePath1, 'w+');
				fwrite($fh1, 'a');
				fclose($fh1);
				//echo 'success';
			}
			else {
				//wrong registration number
				echo '1';
				//echo  'look up the registration number <br>';
			}
		}
		else {
			//wrong default credentials
			echo "-1";
			//echo 'look up the default username, password, and registration number <br>';
		}

	}

?>
