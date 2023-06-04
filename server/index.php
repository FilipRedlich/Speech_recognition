<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Speech Recog db</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <nav>
        Recognized text
    </nav>

    <?php

    include("db.php");

    // Retrieve the recognized text from the request
    @$recognizedText = $_POST['recognized_text'];

    // Processing the recognized text
    $insert = $con->prepare("INSERT INTO `recognized_text`
        VALUES (NULL,?,NOW())");
    $insert->bind_param('s',$recognizedText);
    $insert->execute();

    $result = $con->query("SELECT recognized_text, timestamp from recognized_text");

    while($row = $result->fetch_assoc())  {
        echo $row["recognized_text"] . '<br>';
    } 

    ?>

</body>

</html>