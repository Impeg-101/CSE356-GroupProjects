import requests

base_url = 'http://194.113.73.118'  # Adjust this as necessary

username = "tester"
password = "password"
email = "huifu.li@stonybrook.edu"

def test_login(username, password):
    response = requests.post(f'{base_url}/login', json={'username': username, 'password': password})
    assert response.status_code == 200
    assert check_header(response)
    print('Login test passed')

def test_logout():
    response = requests.get(f'{base_url}/logout')
    assert response.status_code == 200
    assert check_header(response)
    print('Logout test passed')


test_login(username, password)
test_logout()
