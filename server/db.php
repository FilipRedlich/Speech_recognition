<?php
	$host = 'localhost'; //nazwa hosta lub adres IP
	$login = 'root';
	$password = '';
	$dbname = 'speech_recog'; //nazwa bazy danych

	// Create connection
	$con = new mysqli($host, $login, $password, $dbname);

	// Check connection
	if ($con->connect_error) {
		die("Connection failed: " . $con->connect_error);
	}

?>

