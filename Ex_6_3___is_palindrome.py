def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palyndrome(word):
    
    if word == '':
        return True
    
    if first(word) == last(word):
        return is_palyndrome(middle(word))
        
    else:
        return False

s = input("type an word: ")

print('"%s" is palyndrome: '%s, end='')
print(is_palyndrome(s))
