from login_cred_check import login
def test_valid_login():
    assert login("admin", "123") == True


def test_invalid_login():
    assert login("admin", "wrong") == False