def has_no(filename, char):
    fin = open(filename)

    total = 0
    portion = 0

    for line in fin:
        word = line.strip()
        total += 1
        
        if word.find(char) == -1:
            portion += 1
            #print(word)

    print("\ntotal:", total)
    print("'no e' portion:", portion)
    print("%.2f"%(100*portion/total), "% of the words have no 'e'")

has_no("words.txt", 'e')
