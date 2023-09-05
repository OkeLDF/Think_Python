def has_tcd(word):
    counter = 0
    i = 0
    
    while counter < 3 and i < len(word)-1:
        if word[i] == word[i+1]:
            counter += 1
            i += 1

        else:
            counter = 0

        i += 1

    if counter == 3:
        return True
    
    return False

fin = open("words.txt")
total = 0
portion = 0

for word in fin:
    total += 1
    
    if has_tcd(word):
        portion += 1
        print(word.strip())

print("\nTotal:", total)
print("Portion that has three consecutive double letters:", portion)
print("%.6f"%(portion/total), "% of the words has 3 cons double letters")

#print("\nDEBUG: 'ookkee' has 3 cons letters:",has_tcd("ookkee"))
