<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Speech Recog db</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
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

    ?>

    <div class="main-table">
        <table class="table table-responsive">
        <thead>
            <tr class="table-success">
                <td>Rozpoznany text</td>
                <td>Timestamp</td>
            </tr>
            <?php while($row = $result->fetch_assoc())  { ?>
            <tr class="table-data">
                <td>
                    <?=$row['recognized_text']?>
                </td>
                <td>
                    <?=$row['timestamp']?>
                </td>
            </tr>
            <?php } ?>
        </thead>
        </table>

</body>

</html>