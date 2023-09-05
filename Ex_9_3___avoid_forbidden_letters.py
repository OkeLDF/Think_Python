"""
# resposta do livro Think Python:
def avoid(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
"""
# minha tentativa:
def avoid(word, letters):
    for letter in letters:
        if word.find(letter) != -1:
            return False
    return True
""

filename = "words.txt"
fin = open(filename)

s = input("Type the forbidden letters: ")

total = 0
portion = 0

for line in fin:
    word = line.strip()
    total += 1

    if avoid(word, s):
        portion += 1
        #print(word)

print("\ntotal:", total)
print("allowed words portion:", portion)
print("%.2f"%(100*portion/total), "% of the words have no forbidden letters")
