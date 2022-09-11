import pytest

from chapters.ch5 import product_page


@pytest.fixture
def login(py):
    login_with(py, 'standard_user', 'secret_sauce')


def login_with(py, username, password):
    py.visit('https://saucedemo.com')
    py.get('#user-name').type(username)
    py.get('#password').type(password)
    py.get('#login-button').click()


def test_sort_by_name_from_z_to_a(py, login):
    # select the Name (Z to A) sort
    product_page.sort_products_by(py, 'Name (Z to A)')
    # get a list of all item names
    item_names = product_page.get_item_names(py)

    # check if it's in the right order
    expected_item_names = item_names.copy()
    expected_item_names.sort(reverse=True)
    assert expected_item_names == item_names


def test_sort_by_name_from_a_to_z(py, login):
    # select the Name (Z to A) sort
    product_page.sort_products_by(py, 'Name (Z to A)')
    product_page.sort_products_by(py, 'Name (A to Z)')
    # get a list of all item names
    item_names = product_page.get_item_names(py)

    # check if it's in the right order
    expected_item_names = item_names.copy()
    expected_item_names.sort(reverse=False)
    assert expected_item_names == item_names


def test_sort_by_price_low_to_high(py, login):
    # select the price low ti high sort
    product_page.sort_products_by(py, 'Price (low to high)')
    # get a list of all item names
    item_prices = product_page.get_item_prices(py)

    expected_item_prices = item_prices.copy()
    expected_item_prices.sort(reverse=False)
    assert expected_item_prices == item_prices


def test_sort_by_price_high_to_low(py, login):
    # select the price low ti high sort
    product_page.sort_products_by(py, 'Price (high to low)')
    # get a list of all item names
    item_prices = product_page.get_item_prices(py)

    expected_item_prices = item_prices.copy()
    expected_item_prices.sort(reverse=True)
    assert expected_item_prices == item_prices