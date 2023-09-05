"""
# resposta do livro Think Python:
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True
"""
# minha tentativa:
def uses_only(word, letters):
    for letter in word:
        if letters.find(letter) == -1:
            return False
    return True
""

filename = "words.txt"
fin = open(filename)

s = input("Type the letters: ")

total = 0
portion = 0

for line in fin:
    word = line.strip()
    total += 1

    if uses_only(word, s):
        portion += 1
        print(word)

print("\ntotal:", total)
print("portion that uses only ", s, ": ", portion, sep='')
print("%.2f"%(100*portion/total), "% of the words uses only", s)
