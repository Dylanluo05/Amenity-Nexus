<?php
require_once('config.php');
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wght@8..144,200&family=Ubuntu:wght@400;500&display=swap"
          rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <meta charset="UTF-8">
    <title>Sign Up</title>

    {% include "foundation/navigation_bar.html" %}
</head>
<style>

    html, body {
        font-family: 'Roboto Flex', san-serif;
        overflow-x: hidden;
        margin: 0;
        padding: 0;
        background-color: white;
    }

    #account-background-2 {
        height: 1000px;
        background: linear-gradient(to top right, darkblue 0%, purple 100%);
    }

    .signup-link {
        color: blue;
        font-size: 21px;
        text-decoration: underline;
        margin-top: 0px;
        margin-left: 5px;
    }

    .signup-container {
        height: 700px;
        width: 35%;
        background-color: white;
        padding: 11px;
        margin: auto;
        margin-top: 100px;
        box-shadow: 0 10px 10px 0 rgba(0, 0, 0, 0.7);
    }

    .signup-input {
        display: block;
        margin: auto;
        height: 30px;
        padding-left: 7px;
        width: 90%;
        background-color: lightgray;
        border: none;
    }

    .signup-button-1 {
        height: 30px;
        width: 250px;
        color: white;
        background-color: blue;
        border: none;
        display: block;
        margin: auto;
        transition-duration: 0.7s;
    }

    .signup-button-1:hover {
        background-color: lightskyblue;
    }

</style>
<body>

<div>
    <?php
    if(isset($_POST['create'])){
        $email = $_POST['email'];
        $fullname = $_POST['fullname'];
        $password = $_POST['password'];
        $cpassword = $_POST['cpassword'];
    }
    $sql = "INSERT INTO users (email, fullname, password, cpassword) VALUES(?, ?, ?, ?)";
    $stmtinsert = $db->prepare($sql);
    $result = $stmtinsert->execute([$email, $fullname, $password, $cpassword]);
    if($result){
        echo "Works";
    } else {
        echo "Doesn't work :(";
    }
    ?>
</div>
<div id = "account-background-2">
    <br><br>
        <div class="signup-container">
            <h1 style = "margin-top: 10%; text-align: center; color: black;">Sign Up</h1><br>
            <hr style = "display: block; margin-top: -5%;">
            <form id="signup-form" method="post" onsubmit = "signupData()" action="" style = "margin-top: 5%;">
                <h3 style = "text-align: center;">Enter Email</h3>
                <input type = "email" name = "email" placeholder = "Email" class = "signup-input" required>
                <br>
                <h3 style = "text-align: center;">Enter Full Name</h3>
                <input type = "text" name = "full-name" placeholder = "Full Name" class = "signup-input" required>
                <br>
                <h3 style = "text-align: center;">Create a Password</h3>
                <input type = "password" name = "password" placeholder = "Password" class = "signup-input" required>
                <br>
                <h3 style = "text-align: center;">Confirm Password</h3>
                <input type = "password" name = "confirm-password" placeholder = "Confirm Password" class = "signup-input" required>
                <br><br>
                <input type = "submit" value = "Sign In" class = "signup-button-1">
                <br><br>
            </form>
            <p style = "text-align: center; font-size: 21px; margin-top: 0px;">Have an account? <a href = "/sign_in/" class = "signup-link">Sign In</a></p>
        </div>
</div>

<script>
    function signupData() {
        event.preventDefault();
        var signupFormData = $("#signup-form").serializeArray();
    }
</script>

</body>
</html>
