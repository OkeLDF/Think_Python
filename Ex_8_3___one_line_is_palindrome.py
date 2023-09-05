# A step size of -1 goes through the word backwards,
# so the slice [::-1] generates a reversed string.
# Use this idiom to write a one-line version of
# is_palindrome from Exercise 6-3.

def is_palindrome(word):
    return word == word[::-1]

yes = "socorram me em marrocos"
no = "australopiteco"

print(yes,"is palindrome:",is_palindrome(yes))
print(no,"is palindrome:",is_palindrome(no))
