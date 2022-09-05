import challenge_4


def test_win_in_5():
    output = challenge_4.message(5, 6, 20)
    assert output == 'Roll 5: you rolled a 6. You are now on space 20. Congrats, you win!'


def test_win_in_4():
    output = challenge_4.message(4, 5, 20)
    assert output == 'Roll 4: you rolled a 5. You are now on space 20. Congrats, you win!'


def test_lose_over_in_4():
    output = challenge_4.message(4, 6, 24)
    assert output == 'Roll 4: you rolled a 6. You lose and out of field'


def test_lose_over_in_5():
    output = challenge_4.message(5, 3, 21)
    assert output == 'Roll 5: you rolled a 3. You lose and out of field'


def test_lose_under_in_5():
    output = challenge_4.message(5, 2, 11)
    assert output == 'Roll 5: you rolled a 2. You are now on space 11. You lose with 9 to go'