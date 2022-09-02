import coins
#input coins
#check the input
pennies = input('How many pennies do you have? ')
if pennies.isnumeric():
    print(f'You have {coins.sum_pennies(pennies)} coins')
else:
    pennies = input('Please repeat the input ')
nickels = input('How many nickels do you have? ')
if nickels.isnumeric():
    print(f'You have {coins.sum_nickles(nickels)} coins')
else:
    pennies = input('Please repeat the input ')
dimes = input('How many dimes do you have? ')
if dimes.isnumeric():
    print(f'You have {coins.sum_dimes(dimes)} coins')
else:
    pennies = input('Please repeat the input ')
quarters = input('How many quarters do you have? ')
if quarters.isnumeric():
    print(f'You have {coins.sum_quarters(quarters)} coins')
else:
    pennies = input('Please repeat the input ')

#calculate
total = coins.sum_all_coins(pennies=pennies, nickels=nickels, dimes=dimes, quarters=quarters)
#return result
print(coins.generate_result(total))
