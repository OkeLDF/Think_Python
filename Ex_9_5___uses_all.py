"""
# resposta do livro Think Python:
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    return uses_only(required, word)

# This is an example of a program development plan called reduction
# to a previously solved problem, which means that you recognize the
# problem you are working on as an instance of a solved problem and
# apply an existing solution.
"""
# minha tentativa:
def uses_all(word, letters):
    for letter in letters:
        if word.find(letter) == -1:
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

    if uses_all(word, s):
        portion += 1
        print(word)

print("\ntotal:", total)
print("portion that uses all of ", s, ": ", portion, sep='')
print("%.2f"%(100*portion/total), "% of the words uses all of", s)
