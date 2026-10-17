def login(username, password):
    return username == "teacher1" and password == "pass123"

def test_valid_login():
    assert login("teacher1", "pass123") is True
    print("Login test passed")

def test_invalid_login():
    assert login("teacher1", "wrong") is False
    print("Invalid login test passed")

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()