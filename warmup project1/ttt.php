<?php
header('X-CSE356: 65b99885c9f3cb0d090f2059');
// Check if the name is set in the GET request
$name = isset($_GET['name']) ? htmlspecialchars($_GET['name']) : '';

$board = isset($_GET['board']) ? $_GET['board'] : '        ';


function check_winner($xo_array){
    $ttt_checks = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ];

    foreach($ttt_checks as $check){
        if ($xo_array[$check[0]] && 
            $xo_array[$check[1]] && 
            $xo_array[$check[2]] && 
            $xo_array[$check[0]] == $xo_array[$check[1]] && 
            $xo_array[$check[0]] == $xo_array[$check[2]]){
            if($xo_array[$check[0]] == 'X'){
                return 'you';
            }else{
                return 'me';
            }}}

    if(!in_array('',$xo_array)){
        return "none";
    }
    return "";
}

function display_board($board, $name) {

    $board = str_replace('/','',$board);

    $xo_array =  array_fill(0,9,'');
    $index = 0;

    $empty_cells = [];

    foreach (str_split($board) as $char){
        if($char == ' '){
            $index++;
        }else{
            $xo_array[$index] = $char;
        }
    }

    for($i=0;$i<9;$i++){
        if(!$xo_array[$i]){
            $empty_cells[] = $i;
        }
    }

    $winner = check_winner($xo_array);

    if($winner == "you"){
        echo "You Win!";
        echo "<a href='http://localhost/CSE356/ttt.php?name=$name'>Play Again</a>";
    }else if($winner == "me"){
        echo "I Win!";
        echo "<a href='http://localhost/CSE356/ttt.php?name=$name'>Play Again</a>";
    }else if($winner == "none"){
        echo "WINNER: NONE.  A STRANGE GAME.  THE ONLY WINNING MOVE IS NOT TO PLAY.";
    }

    if($winner == "" && substr_count($board, 'O') < substr_count($board, 'X')){
        $server_cell = $empty_cells[random_int(0, count($empty_cells)-1)];
        $xo_array[$server_cell] = 'O';
    }

    $winner = check_winner($xo_array);

    if($winner == "me"){
        echo "I Win!";
        echo "<a href='http://localhost/CSE356/ttt.php?name=$name'>Play Again</a>";
    }


    //else:
    $board = implode(' ',$xo_array);
    echo "<table>"; // Start table for grid layout
    for ($cell = 0; $cell < 9; $cell++) {
        if ($cell % 3 == 0) echo "<tr>"; // Start new row every 3 cells

        echo "<td>";
        $cell_char = $xo_array[$cell];
        // Check if the cell is empty
        if ($cell_char == '') {

            $position = 0;

            $space_visited = 0;

            foreach (str_split($board) as $char){
                if($space_visited == $cell){break;}
                if($char == ' '){
                    $space_visited++;
                }
                $position++;
            }

            $next_board = substr($board, 0, $position) . 'X' . substr($board, $position);
            if($winner == ""){
                 echo "<a href='http://localhost/CSE356/ttt.php?name=$name&board=$next_board'>Move</a>";
            }
        } else {
            echo $cell_char;
        }
        echo "</td>";

        if ($cell % 3 == 2) echo "</tr>";
    }
    echo "</table>";
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
        }

        table {
            border-collapse:collapse;
            margin: auto;
        }

        td {
            padding: 50px;
            width: 50px;
            height: 50px;
            text-align: center;
            vertical-align: middle;
            border: solid 2px;
        }

    </style>
</head>
<body>
    <?php if ($name): ?>
        <p><?= "Hello " . $name . ", " . date("Y-m-d") ?></p>
        <?php display_board($board, $name);?>
    <?php else: ?>
    <form action="/ttt.php" method="get">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <button type="submit">Submit</button>
    </form>
    <?php endif;?>
</body>
</html>
