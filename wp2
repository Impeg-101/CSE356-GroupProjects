<?php
header('X-CSE356: 65b99885c9f3cb0d090f2059');
session_start();


$path = explode('.php/', $_SERVER['REQUEST_URI'])[1];
$path = explode('?', $path)[0];

echo $path;
echo "<br/>";


switch ($path) {
    case 'adduser':
        if ($_SERVER['REQUEST_METHOD'] == 'GET' && isset($_GET['username']) && isset($_GET['password']) && isset($_GET['email'])) {
            $username = $_GET['username'];
            $password = $_GET['password'];
            $email = $_GET['email'];
        
            $key = md5(rand());
        
            $_SESSION['user'] = [
                'username' => $username,
                'password' => $password,
                'email' => $email,
                'key' => $key
            ];
        
            $verificationLink = "http://localhost/cse356/wp2.php/verify?email=$email&key=$key";
            // mail($email, 'Verify Your Email', "Please click on this link to verify your email: $verificationLink");
        
            echo "<br/>";
            echo $verificationLink;
            echo "<br/>";
        
            echo 'User created successfully. Please check your email to verify.';
        }
        break;
    case 'verify':
        if ($_SERVER['REQUEST_METHOD'] == 'GET' && isset($_GET['email']) && isset($_GET['key'])) {
            $email = $_GET['email'];
            $key = $_GET['key'];
            
            $user = $_SESSION['user'];

            if ($user['email'] === $email && $user['key'] === $key) {
                echo 'Email verified successfully!<br/>';
                echo "http://localhost/cse356/wp2.php/login?username=" . $_SESSION['user']['username'] . "&password=" . $_SESSION['user']['password'];
                return;
            }
            echo 'Verification failed.';
            print_r($_SESSION['user']);
            
        }
        break;
    case 'login':
        if ($_SERVER['REQUEST_METHOD'] == 'GET' && isset($_GET['username']) && isset($_GET['password'])) {
            $username = $_GET['username'];
            $password = $_GET['password'];
        
            $user = $_SESSION['user'];

            if($user["username"] == $username && $user["password"] == $password){
                echo "Verification sucess";
            }else{
                echo 'Verification failed.';
            }
        }
        break;
    default:
        echo "404 Not Found";
        break;
}


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Warm Up Project 2</title>
</head>
<body>
</body>
</html>
