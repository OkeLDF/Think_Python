for i in range(0, 11):
    print(i)
    for n in range(0, 150):
        if n>=100:
            me = str(n).zfill(3)
            mom = str(n + 9*i)[::-1].zfill(3)
        else:
            me = str(n).zfill(2)
            mom = str(n + 9*i)[::-1].zfill(2)
    
        if me == mom:
            print("  ", me)
