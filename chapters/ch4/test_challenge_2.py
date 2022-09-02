import challenge_2


def test_palindrome_with_spaces():
    check = challenge_2.is_palindrome(' abcdedcba   ')
    assert check == 'Palindrome it is!'


def test_palindrome_letters_numbers():
    check = challenge_2.is_palindrome('1numun1')
    assert check == 'Palindrome it is!'


def test_palindrome_numbers_spaces():
    check = challenge_2.is_palindrome('45654   ')
    assert check == 'Palindrome it is!'


def test_palindrome_uppercase_lowercase():
    check = challenge_2.is_palindrome('TWOowt')
    assert check == 'Palindrome it is!'


def test_not_palindrome():
    check = challenge_2.is_palindrome('abcdefg')
    assert check == 'Not a palindrome'


def test_not_palindrome_with_numbers():
    check = challenge_2.is_palindrome('12abcdefg123')
    assert check == 'Not a palindrome'