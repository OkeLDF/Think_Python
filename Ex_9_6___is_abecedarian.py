"""
# indícios de mentalidade de programador em C...
def is_abecedarian(word):
    for i in range(len(word)):
        for j in range(i, len(word)):
            if word[i] > word[j]:
                return False
    return True
"""

# agora sim, como um programador em Python...
def is_abecedarian(word):
    for i in word:
        for j in word[word.find(i):]:
            if i > j:
                return False
    return True

"""
# alternativa recursiva do livro Think Python:
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])
"""

filename = "words.txt"
fin = open(filename)

total = 0
portion = 0

for line in fin:
    word = line.strip()
    total += 1

    if is_abecedarian(word):
        portion += 1
        print(word)

print("\ntotal:", total)
print("abecedarian portion:", portion)
print("%.2f"%(100*portion/total), "% of the words are abecedarian")
