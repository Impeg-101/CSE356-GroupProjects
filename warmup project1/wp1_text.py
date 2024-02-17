import requests
from bs4 import BeautifulSoup

def test_ttt_page():
    print("\nTic Tac Toe test")
    url = f"http://{ip_address}/CSE356/ttt.php"

    response_name_form = requests.get(url, headers=headers)
    assert "name" in response_name_form.text, "Initial page does not have 'name' field!\n" + response_name_form.text
    print("Passed : Name form page")

    name = "TestUser"
    response_game_page = requests.get(url, params={"name": name}, headers=headers)
    soup = BeautifulSoup(response_game_page.text, 'html.parser')
    board = soup.find('a', {'href': True})

    assert f"Hello {name}" in response_game_page.text, "Name not displayed correctly in game!\n" + response_game_page.text
    print("Passed : In game greeting")
    assert board is not None, "Tic-Tac-Toe board not found!\n" + response_game_page.text
    print("Passed : In game board display")

    move_link = board['href']
    response = requests.get(move_link, headers=headers)
    assert "X" in response.text, "Tic-Tac-Toe move not registered"
    print("Passed : Maken valid move in game")

    # Test for win, lose, and tie ...


def test_connect_page():
    print("\nConnect4 test")
    url = f"http://{ip_address}/CSE356/connect.php"

    response_name_form = requests.post(url, headers=headers)
    assert "name" in response_name_form.text, "Initial page does not have 'name' field!\n" + response_name_form.text
    print("Passed : Name form page")

    name = "TestUser"
    response_game_page = requests.post(url, data={"name": name}, headers=headers)
    assert f"Hello {name}" in response_game_page.text, "Name not displayed correctly in game!\n" + response_game_page.text
    print("Passed : In game greeting")

    soup = BeautifulSoup(response_game_page.text, 'html.parser')
    board_button = soup.find('button', {'name': "board", "type":"submit"})
    assert board_button is not None, "Board not found!\n" + response_game_page.text
    print("Passed : In game board display")

    move_data = {"name" : board_button["name"], "value" : board_button["value"]}
    response = requests.post(url, data=move_data, headers=headers)
    assert "X" in response.text, "Move not registered"
    print("Passed : Maken valid move in game")

    # Test for win, lose, and tie ...

def test_battleship_page():
    print("\nBattleship test")
    url = f"http://{ip_address}/CSE356/battleship.php"

    response_name_form = requests.post(url, headers=headers)
    assert "name" in response_name_form.text, "Initial page does not have 'name' field!\n" + response_name_form.text
    print("Passed : Name form page")

    name = "TestUser"
    response_game_page = requests.post(url, data={"name": name}, headers=headers)
    assert f"Hello {name}" in response_game_page.text, "Name not displayed correctly in game!\n" + response_game_page.text
    assert ">?<" in response_game_page.text, "Board not initialized with all '?' " + response_game_page.text
    print("Passed : In game greeting")

    soup = BeautifulSoup(response_game_page.text, 'html.parser')
    board_button = soup.find('button', {'name': "move", "type":"submit"})
    assert board_button is not None, "Board not found!\n" + response_game_page.text
    print("Passed : In game board display")

    move_data = {"name" : board_button["name"], "value" : board_button["value"]}
    response = requests.post(url, data=move_data, headers=headers)
    assert "X" in response.text or "O" in response.text, "Move not registered"
    print("Passed : Maken valid move in game")

    # Test for win, lose, and tie ...


ip_address = "localhost"
headers = {"X-CSE356": "65b99885c9f3cb0d090f2059"}

test_ttt_page()
test_connect_page()
test_battleship_page()
print("All tests passed successfully!")
