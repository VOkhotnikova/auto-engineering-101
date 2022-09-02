def sum_pennies(user_input):
    pennies = int(user_input)
    return pennies


def sum_nickles(user_input):
    nickles = 5 * int(user_input)
    return nickles


def sum_dimes(user_input):
    dimes = 10 * int(user_input)
    return dimes


def sum_quarters(user_input):
    quarters = 25 * int(user_input)
    return quarters


def sum_all_coins(pennies, nickels, dimes, quarters):
    return sum([
        sum_pennies(pennies),
        sum_nickles(nickels),
        sum_dimes(dimes),
        sum_quarters(quarters)
    ])


def generate_result(total):
    if total == 100:
        return 'You win!'
    elif total < 100:
        under = 100 - total
        return f'You lose... You were under by {under} cents'
    else:
        over = total - 100
        return f'You lose... You were over by {over} cents'