def is_palindrome(word):
    word = word.lower().strip()
    for i in range(len(word) // 2):
        if word[i] == word[-i-1]:
            continue
        else:
            return 'Not a palindrome'
    return 'Palindrome it is!'


if __name__ == '__main__':
    check = input('Please enter a palindrome: ')
    print(is_palindrome(check))