from selenium.webdriver import Keys


def test_search_for_puppies(py):
    py.visit('https://www.google.com/')
    py.get("[name='q']").type('puppies', Keys.ENTER)
    # py.get("[name='btnK']").submit()
    assert py.should().contain_title('puppies')


# def test_carlos_is_on_leadership(py):
#     py.visit('https://qap.dev')
#     py.get('a[href="/about"]').hover()
#     py.get('a[href="/leadership"][class^="Header-nav"]').click()
#     assert py.contains('Carlos Kidman')
#
#
# def test_carlos_is_on_leadership_2(py):
#     py.visit('https://qap.dev')