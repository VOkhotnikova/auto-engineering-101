def count_vowels(words):
    count = 0
    for ch in words.lower():
        if ch in 'aeiouy':
            count +=1
    return count


if __name__ == '__main__':
    phrase = input('Please input a phrase to count vowels: ')
    print(count_vowels(phrase))