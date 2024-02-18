import requests
from bs4 import BeautifulSoup

def test_ttt_page():
    print("\nTic Tac Toe test")
    url = f"http://{ip_address}/CSE356/ttt.php"

    response_name_form = requests.get(url, headers=headers)
    assert "name" in response_name_form.text, "Initial page does not have 'name' field!\n" + response_name_form.text
    print("Passed : Name form page")

    name = "TestUser"
    response = requests.get(url, params={"name": name}, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    board = soup.find('a', {'href': True})

    assert f"Hello {name}" in response.text, "Name not displayed correctly in game!\n" + response.text
    print("Passed : In game greeting")
    assert board is not None, "Tic-Tac-Toe board not found!\n" + response.text
    print("Passed : In game board display")

    move_link = board['href']
    response = requests.get(move_link, headers=headers)
    assert "X" in response.text, "Tic-Tac-Toe move not registered"
    print("Passed : Maken valid move in game")

    # Test for win, lose, and tie ...

def display_board(board):
    last_c = ""
    for c in board:
        print(c, end="")
        if(last_c == " " and c == " "):
            print(" ", end="")
        if(c == '.'):
            print("\n", end="")
        last_c = c
    print()

def test_connect_page():
    print("\nConnect4 test")
    url = f"http://{ip_address}/CSE356/connect.php"

    response_name_form = requests.post(url, headers=headers)
    assert "name" in response_name_form.text, "Initial page does not have 'name' field!\n" + response_name_form.text
    print("Passed : Name form page")

    name = "TestUser"
    response = requests.post(url, data={"name": name}, headers=headers)
    assert f"Hello {name}" in response.text, "Name not displayed correctly in game!\n" + response.text
    print("Passed : In game greeting")

    soup = BeautifulSoup(response.text, 'html.parser')
    board_button = soup.find('button', {'name': "board", "type":"submit"})
    assert board_button is not None, "Board not found!\n" + response.text
    print("Passed : In game board display")

    move_data = {"name" : name, "board" : board_button["value"]}
    response = requests.post(url, data=move_data, headers=headers)
    assert "X" in response.text, "Move not registered"
    print("Passed : Maken valid move in game")

    # Test for win, lose, and tie ...

    board = "      .      .      .      .      .X X X X O O O"
    move_data = {"name" : name, "board" : board}
    response = requests.post(url, data=move_data, headers=headers)
    assert "You won" in response.text, response.text + "\nError occured in a game that is won"
    assert "Play Again" in response.text, response.text + "\nNo Play Again button"
    print("Passed : Winning")

    board = "      .      .      .      .      .X X X O O O O"
    move_data = {"name" : name, "board" : board}
    response = requests.post(url, data=move_data, headers=headers)
    assert "I won" in response.text, response.text + "\nError occured in a game that is lost"
    assert "Play Again" in response.text, response.text + "\nNo Play Again button"
    print("Passed : Losing")

    board = "X X O O O X X.X O X X X O X.O X O O O X O.O O X X X O O.O X X O X X O.X X X O X X X"
    move_data = {"name" : name, "board" : board}
    response = requests.post(url, data=move_data, headers=headers)
    assert "Draw" in response.text, response.text + "\nError occured in a game that is tied"
    assert "Play Again" in response.text, response.text + "\nPlay Again button exist in a tied game"
    print("Passed : Losing")


def test_battleship_page():
    print("\nBattleship test")
    url = f"http://{ip_address}/CSE356/battleship.php"

    session = requests.Session()

    response_name_form = session.post(url, headers=headers)
    assert "name" in response_name_form.text, "Initial page does not have 'name' field!\n" + response_name_form.text
    print("Passed : Name form page")

    name = "TestUser"
    response = session.post(url, data={"name": name}, headers=headers)
    assert f"Hello {name}" in response.text, "Name not displayed correctly in game!\n" + response.text
    assert ">?<" in response.text, "Board not initialized with all '?' " + response.text
    print("Passed : In game greeting")

    soup = BeautifulSoup(response.text, 'html.parser')
    board_button = soup.find('button', {'name': "move", "type":"submit"})
    assert board_button is not None, "Board not found!\n" + response.text
    assert "Moves left: 21" in response.text, response.text + "\nMoves left not found!"
    print("Passed : Game initilization")

    moves = [
        {0,0},{0,1},{0,2},{0,3},{0,4},{0,5},{0,6},
        {1,0},{1,1},{1,2},{1,3},{1,4},{1,5},{1,6},
        {2,0},{2,1},{2,2},{2,3},{2,4},{2,5},{2,6},
        {3,0},{3,1},{3,2},{3,3},{3,4},{3,5},{3,6},
        {4,0},{4,1},{4,2},{4,3},{4,4},{4,5},{4,6}
    ]

    response = session.post(url, data={"move" : "2,0"}, headers=headers)
    assert ">X<" in response.text or ">O<" in response.text, response.text + "\nMove not registered"
    assert "Moves left: 20" in response.text, response.text + "\nMove count did not decrease"
    print("Passed : Maken valid move in game") 

    response = session.post(url, data={"move" : "2,1"}, headers=headers)
    response = session.post(url, data={"move" : "3,0"}, headers=headers)
    response = session.post(url, data={"move" : "3,1"}, headers=headers)
    response = session.post(url, data={"move" : "3,2"}, headers=headers)
    response = session.post(url, data={"move" : "4,0"}, headers=headers)
    response = session.post(url, data={"move" : "4,1"}, headers=headers)
    response = session.post(url, data={"move" : "4,2"}, headers=headers)
    
    # Test for win, lose, and tie ...
    
    response = session.post(url, data={"move" : "4,3"}, headers=headers)
    assert "You won" in response.text, response.text + "\nError occured in a game that is won"
    assert "Play Again" in response.text, response.text + "\nNo Play Again button"
    print("Passed : Winning")

    


ip_address = "localhost"
headers = {"X-CSE356": "65b99885c9f3cb0d090f2059"}

test_ttt_page()
test_connect_page()
test_battleship_page()
print("All tests passed successfully!")
exit()

for i in range(0, 5):
    for j in range(0, 7):
        print("{",end="")
        print(f"{i},{j}",end="")
        print("},",end="")


exit()

import random

all_moves = [
    [0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],
    [1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],
    [2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],
    [3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],
    [4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[4,6],
    [5,0],[5,1],[5,2],[5,3],[5,4],[5,5],[5,6]
]

matrix = [
    ["-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-"]
]

# 0 for empty cell
# 1 for X
# -1 for O

def check_winner():

    total_empty_cells = 0
    
    for row in range(0,6):
        for col in range(0,7):
            cell = matrix[row][col]
            if (cell == '-'):
                total_empty_cells += 1
                continue

            if ((col <= 3 and cell == matrix[row][col + 1] and cell == matrix[row][col + 2] and cell == matrix[row][col + 3]) or
                (row <= 2 and cell == matrix[row + 1][col] and cell == matrix[row + 2][col] and cell == matrix[row + 3][col]) or
                (row <= 2 and col <= 3 and cell == matrix[row + 1][col + 1] and cell == matrix[row + 2][col + 2] and cell == matrix[row + 3][col + 3]) or
                (row <= 2 and col >= 3 and cell == matrix[row + 1][col - 1] and cell == matrix[row + 2][col - 2] and cell == matrix[row + 3][col - 3])):

                return True, cell
            
    return True if total_empty_cells == 0 else False, ""

x_turn = True

for _ in range(10):
    while 1:
        index = random.randint(0,len(all_moves)-1)
        _, col = all_moves[index]
        row = 0

        while row < 5 and matrix[row+1][col] == '-':
            row += 1

        for i in range(0,len(all_moves)):
            if row == all_moves[i][0] and col == all_moves[i][1]:
                all_moves.pop(i)
                break

        matrix[row][col] = "X" if x_turn else "O"
        x_turn = not x_turn

        over, side = check_winner()

        if over:
            board = ""
            text = ""
            message = ""
            passed = ""
            for row in range(0,6):
                for col in range(0,7):
                    cell = matrix[row][col]
                    # print(cell, end=(" " if col < 6 else ""))
                    board += "" if cell == "-" else cell
                    board += " " if col < 6 else ""
                # print('.')
                board += "." if row < 5 else ""

            if side == "":
                text = "WINNER: NONE.  A STRANGE GAME.  THE ONLY WINNING MOVE IS NOT TO PLAY."
                message = "Error occured in a game that is tied"
                passed = "Tied game"
            elif side == "X":
                text = "You won"
                message = "Error occured in a game that is won"
                passed = "Winning"
            elif side == "O":
                text = "I won"
                message = "Error occured in a game that is lost"
                passed = "Losing"

            print(f"    board = \"{board}\"")
            print("    move_data = {\"name\" : name, \"board\" : board}")
            print(f"    response = requests.post(url, data=move_data, headers=headers)")
            print(f"    assert \"{text}\" in response.text, response.text + \"\\n{message}\"")
            print(f"    print(\"Passed : {passed}\")\n\n")

            break