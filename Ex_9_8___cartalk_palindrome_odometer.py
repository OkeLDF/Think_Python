def is_palindrome(word):
    return word == word[::-1]

def has_palindrome(word, start, lenght):
    """
    word: str
    start: int
    lenght: int
    """
    s = word[ start : (start + lenght) ]
    return s == s[::-1]

def magic_odom(i):
    "i: int"
    return (has_palindrome(str(i), 2, 4) and
            has_palindrome(str(i+1), 1, 5) and
            has_palindrome(str(i+2), 1, 4) and
            is_palindrome(str(i+3)))

def checkall():
    for i in range(100000, 1000000):
        if magic_odom(i):
            print(i)

checkall()
