import pytest


@pytest.fixture
def login_with(py, username, password):
    py.visit('https://saucedemo.com')
    py.get('#user-name').type(username)
    py.get('#password').type(password)
    py.get('#login-button').click()