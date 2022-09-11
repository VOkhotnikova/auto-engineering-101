import pytest


@pytest.fixture
def login(py):
    login_with(py, 'standard_user', 'secret_sauce')


def login_with(py, username, password):
    py.visit('https://saucedemo.com')
    py.get('#user-name').type(username)
    py.get('#password').type(password)
    py.get('#login-button').click()


def test_user_can_login(py, login):
    py.contains('Add to cart').click()
    py.get("[class='shopping_cart_link']").click(force=True)
    py.contains('Checkout').click(force=True)
    assert py.should().contain_url('checkout-step-one.html')


# def test_user_can_logout(py, login):
#     py.get('[class="bm-burger-button"]').click()
#     py.get("[id='logout_sidebar_link']").click(force=True)
#     assert py.should().contain_url('index.html')