def right_justify(s):
    #lines = len(s)//70
    white_spaces = 70 - len(s)

    for i in range(white_spaces):
        print(" ", end='')

    print(s)

s = input("Digite algum texto: ")
right_justify(s)
