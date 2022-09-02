import challenge_1


def test_regular_case():
    words = 'who let the dogs out'
    output = challenge_1.count_vowels(words)
    assert output == 6


def test_all_uppercase_letters():
    words = 'WHO LET THE DOGS OUT'
    output = challenge_1.count_vowels(words)
    assert output == 6


def test_all_numbers_no_vowels():
    output = challenge_1.count_vowels('123456789')
    assert output == 0


def test_all_vowes():
    output = challenge_1.count_vowels('aeiouy')
    assert output == 6