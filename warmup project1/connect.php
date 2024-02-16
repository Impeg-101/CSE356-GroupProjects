<?php

function check_winner($matrix){
    
    for($row=5; $row >= 0; $row--){
        for($col=6; $col >= 0; $col--){
            $cell = $matrix[$row][$col];
            if ($cell == "") {
                continue;
            }

            if ($col <= 3 && $cell == $matrix[$row][$col + 1] && $cell == $matrix[$row][$col + 2] && $cell == $matrix[$row][$col + 3]) {
                return [[$row, $col], [$row, $col + 1], [$row, $col + 2], [$row, $col + 3]];
            }

            if ($row <= 2 && $cell == $matrix[$row + 1][$col] && $cell == $matrix[$row + 2][$col] && $cell == $matrix[$row + 3][$col]) {
                return [[$row, $col], [$row + 1, $col], [$row + 2, $col], [$row + 3, $col]];
            }

            if ($row <= 2 && $col <= 3 && $cell == $matrix[$row + 1][$col + 1] && $cell == $matrix[$row + 2][$col + 2] && $cell == $matrix[$row + 3][$col + 3]) {
                return [[$row, $col], [$row + 1, $col + 1], [$row + 2, $col + 2], [$row + 3, $col + 3]];
            }

            if ($row <= 2 && $col >= 3 && $cell == $matrix[$row + 1][$col - 1] && $cell == $matrix[$row + 2][$col - 2] && $cell == $matrix[$row + 3][$col - 3]) {
                return [[$row, $col], [$row + 1, $col - 1], [$row + 2, $col - 2], [$row + 3, $col - 3]];
            }
        }
    }
    return [];
}

function display_board(){

    $name = isset($_POST['name']) ? htmlspecialchars($_POST['name']) : "";

    if($name == ""){
        echo '<label for="name">Name:</label>
            <input type="text" id="name" name="name">
            <button type="submit">Submit</button>';
        return;
    }

    $board = isset($_POST['board']) ? urldecode($_POST['board']) : '';

    echo "<p>Hello, " . $name . ", " .  date("Y-m-d") .  "!</p>";

    // turn board string into an array

    $matrix = [
        ["","","","","","",""],
        ["","","","","","",""],
        ["","","","","","",""],
        ["","","","","","",""],
        ["","","","","","",""],
        ["","","","","","",""]
    ];

    $row = 0;
    $col = 0;
    // add each string into corresponding array spot
    for ($i = 0; $i < strlen($board); $i++) {
        $char = $board[$i];
        if($char == " "){
            $col++;
        }else if($char == '.'){
            $col = 0;
            $row++;
        }else{
            $matrix[$row][$col] = $char;
        }
    }

    // check which spots are available for guesses
    $open_cells = [];

    for($i=0; $i<6; $i++){
        for($j=0; $j<7; $j++){
            if($matrix[$i][$j] == ""){
                $open_cells[] = [$i,$j];
            }
        }
    }
    
    //check winner after each move

    $winner = 0;

    $winner_cells = check_winner($matrix);
    
    if(count($winner_cells) > 0){
        $cell = $winner_cells[0];
        if($matrix[$cell[0]][$cell[1]] == "X"){
            $winner = 1;
        }else{
            $winner = -1;
        }
    }

    if($winner == 0 && $board != ""){
        // add a random move

        $rand_col = random_int(0,6);

        $row = 0;
        while($row < 5){
            if($matrix[$row+1][$rand_col] == ""){
                $row++;
            }else{
                break;
            }
        }
        $matrix[$row][$rand_col] = "O";

        $winner_cells = check_winner($matrix);
    
        if(count($winner_cells) > 0){
            $cell = $winner_cells[0];
            if($matrix[$cell[0]][$cell[1]] == "X"){
                $winner = 1;
            }else{
                $winner = -1;
            }
        }
    }

    echo "<table>";
    echo "<tr>";
    for ($j = 0; $j < 7; $j++) {
        echo "<td>";
        if($winner != 0){
            echo "";
        }else if($matrix[0][$j] == ""){
            // if top is not full then find the one row that is not full in a column
            $row = 0;
            while($row < 5){
                if($matrix[$row+1][$j] == ""){
                    $row++;
                }else{
                    break;
                }
            }

            $matrix[$row][$j] = 'X';

            $matrix_row_string = [
                implode(' ',$matrix[0]),
                implode(' ',$matrix[1]),
                implode(' ',$matrix[2]),
                implode(' ',$matrix[3]),
                implode(' ',$matrix[4]),
                implode(' ',$matrix[5])
            ];

            $matrix[$row][$j] = '';
            
            $matrix_string = implode('.',$matrix_row_string);

            echo "<button type='submit' name='board' value='" . urlencode($matrix_string) . "'>$j</button>";


        }else{
            echo "Full";
        }
        echo "</td>";
    }
    echo "</tr>";

    for ($i = 0; $i < 6; $i++) {
        echo "<tr>";
        for ($j = 0; $j < 7; $j++) {
            $class = "";
            foreach($winner_cells as $cell){
                if($cell[0] == $i && $cell[1] == $j){
                    $class = "winner";
                }
            }

            echo "<td class='$class'>";
            echo $matrix[$i][$j]; 
            echo "</td>";
        }
        echo "</tr>";
    }
    
    echo "</table>";
    if($winner > 0){
        echo "You won!";
        echo "<br/><button type='submit' name='board' value=''>Play again</button>";
    }else if($winner < 0){
        echo "I won!";
        echo "<br/><button type='submit' name='board' value=''>Play again</button>";
    }else{
        $full_board = implode("",[
                                    implode("",$matrix[0]),
                                    implode("",$matrix[1]),
                                    implode("",$matrix[2]),
                                    implode("",$matrix[3]),
                                    implode("",$matrix[4]),
                                    implode("",$matrix[5])
                                ]);
        if(strlen($full_board) == 42){
            echo "Draw";
            echo "<br/><button type='submit' name='board' value=''>Play again</button>";
        }
    }
    echo '<input type="hidden" name="name" value="' . $name . '">';
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
            border: solid 2px;
        }

        .winner{
            background-color: #AAFF00;
        }

    </style>
</head>
<body>
    <form action="/connection.php" method="post">
        <?php display_board();?>
    </form>
</body>
</html>
