<?php
	$file = $_POST['picture'];
	//$image = imagecreatefromjpeg($file);
	//imagealphablending($image, false);
	//imagesavealpha($image, true);

	//ob_start();
	//header('Content-Description: File Transfer');
	//header('Content-Type: image/jpg');
	//header('Content-Disposition: attachment; filename="'.$file'"');
	//header('Content-Transfer-Encoding: binary');
	//header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
	//header('Pragma: public');
	$imgbinary = fread(fopen($file, "r"), filesize($file));
	$img_str = base64_encode($imgbinary);

	//$contents = ob_get_contents();
	//ob_get_flush();


	echo $img_str;


	//imagedestroy($image);
?>
