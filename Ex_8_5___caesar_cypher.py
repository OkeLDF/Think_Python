def signal(x):
    return int(x/abs(x))

def __cond__(letter_is_lower, char):
    if letter_is_lower:
        return char < 97 or char > 122
    else:
        return char < 65 or char > 90

def rotate(word, times):
    s = ''

    for letter in word:
        char = ord(letter) + times

        if __cond__(letter.islower(), char):
            char += 26 * -signal(times)
        
        s += chr(char)

    return s

print(rotate('melon', -10))
print(rotate('Oke', -2))
print(rotate('RUJA', 14))
print(rotate('Oui', 10)) # 'oui' is 'yes' in french lol
