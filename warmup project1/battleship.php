<?php
header('X-CSE356: 65b99885c9f3cb0d090f2059');
session_start();

$name = isset($_POST["name"]) ? htmlspecialchars($_POST["name"]) : "";

function initializeGame(){
    $_SESSION["moves_left"] = ceil(7 * 5 * 0.60);
    $_SESSION["board_state"] = [
        ["?","?","?","?","?","?","?"],
        ["?","?","?","?","?","?","?"],
        ["?","?","?","?","?","?","?"],
        ["?","?","?","?","?","?","?"],
        ["?","?","?","?","?","?","?"]
    ];
    $_SESSION["secret_locations"] = [
        [2,0],
        [2,1],
        [3,0],
        [3,1],
        [3,2],
        [4,0],
        [4,1],
        [4,2],
        [4,3]
    ];
    $_SESSION["winner"] = 0;
}

if(strlen($name) > 0 && !isset($_SESSION["name"])){
    $_SESSION["name"] = $name;
    initializeGame();
}

function check_winner($matrix){

}

function display_board(){

    if(session_status() == PHP_SESSION_NONE || !isset($_SESSION["name"])){
        //display the form for inputting the name
        echo '<label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <button type="submit">Submit</button>';
        return;
    }
    
    echo "<p>Hello " . $_SESSION["name"] . ", " .  date("Y-m-d") .  "</p>";

    $move_string = isset($_POST["move"]) ? $_POST["move"] : '';
    
    if(strlen($move_string) > 0){
        $move_array = explode(",", $move_string);
        $moves = [intval($move_array[0]),intval($move_array[1])];

        if($_SESSION["board_state"][$moves[0]][$moves[1]] == "?"){
            $hit_or_miss = "O";

            //check if the moves are hit or miss
            foreach($_SESSION["secret_locations"] as $key => $location){
                if($location[0] == $moves[0] && $location[1] == $moves[1]){
                    $hit_or_miss = "X";
                    unset($_SESSION["secret_locations"][$key]);
                    break;
                }
            }

            $_SESSION["board_state"][$moves[0]][$moves[1]] = $hit_or_miss;
            $_SESSION["moves_left"]--;
        }
    }else{
        initializeGame();
    }
    
    if(count($_SESSION["secret_locations"]) == 0){
        $_SESSION["winner"] = 1;
    }else if($_SESSION["moves_left"] == 0){
        $_SESSION["winner"] = -1;
    }

    echo "Moves left: " . $_SESSION["moves_left"];
    echo "<table>";
    for($row=0; $row < 5 ; $row++){
        echo "<tr>";
        for($col=0; $col < 7; $col++){
            
            $input = "name='move' value='$row,$col'>";

            if($_SESSION["board_state"][$row][$col] != "?" || $_SESSION["winner"] != 0){
                $input = "disabled>";
            }

            echo "<td>";
            echo "<button type='submit' " . $input . $_SESSION["board_state"][$row][$col] ."</button>";
            echo "</td>";

        }
        echo "</tr>";
    }
    echo "</table>";

    if($_SESSION["winner"] > 0){
        echo "You won!";
        echo "<br/><button class='play-again-button' type='submit' name='move' value=''>Play Again</button>";
    }else if($_SESSION["winner"] < 0){
        echo "I won!";
        echo "<br/><button class='play-again-button' type='submit' name='move' value=''>Play Again</button>";
    }else{
        echo "Can you find where my ships are?<br/>";
    }
}



?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Warm Up Project</title>
    <style>
        body {
            background-color: white;
            display: flex;
            align-content: center;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        table {
            border-collapse:collapse;
            margin: auto;
        }

        td {
            width: 50px;
            height: 50px;
            text-align: center;
            vertical-align: middle;
            /* border: solid 2px; */
        }

        button {
            height: 100%;
            width: 100%;
            border: none;
            border-radius: 10%;
            background-color: #000080;
            color: white;
        }

        button:hover{
            background-color: lightblue;
            color: black;
        }

        .play-again-button {
            width: 80px;
            border: solid black 2px;
            border-radius: 10px;
            background-color: white;
            color: black;
        }

        .play-again-button:hover {
            background-color: lightgreen;
        }

    </style>
</head>
<body>
    <form action="/battleship.php" method="post">
        <?php display_board();?>
    </form>
</body>
</html>
