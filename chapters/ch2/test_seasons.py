from seasons import whats_the_season


def test_autumn1():
    output = whats_the_season('fall')
    assert output == 'leaves'


def test_autumn2():
    output = whats_the_season('AuTumn')
    assert output == 'leaves'


def test_summer():
    output = whats_the_season('SUMMER')
    assert output == 'beach'


def test_spring():
    output = whats_the_season('spriNG')
    assert output == 'flowers'


def test_winter():
    output = whats_the_season(' winter  ')
    assert output == 'snow'


def test_wrong_input():
    wrong = whats_the_season('any')
    assert wrong == 'I don`t know that season'


def test_wrong_input_numbers():
    wrong = whats_the_season('12357any')
    assert wrong == 'I don`t know that season'