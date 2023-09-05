# finder:

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

# "As an exercise, modify find so that it has a third parameter:
# the index in word where it should start looking."

def find_s(word, letter, start):
    i = start
    while i < len(word):
        if word[i] == letter:
            return i
        i += 1
    return -1

# counter:

def count(word, letter):
    c = 0
    for w in word:
        if w == letter:
            c += 1
    return c

# "rewrite the function so that instead of traversing the string,
# it uses the threeparameter version of find from the previous section."

def count_s(word, letter, start):
    i = find_s(word, letter, start)
    if i == -1:
        return 0
    
    return 1 + count_s(word, letter, i+1)

# finders:
print(find("banana", "n"))
print(find_s("Arthur, the king of the britons", "k", 10))

# counters:
print(count("arara", "a"))
print(count_s("Tres pratos de trigo para tres tigres tristes", "r", 0))
