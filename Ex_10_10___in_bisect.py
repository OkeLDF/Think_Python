#####################
# Tá tudo errado... #
#####################

'''
def in_bisect(t, search):
    mid = int(len(t) / 2)
    
    print("search:", search," mid:", mid, " t:", t)

    #if mid == 0:
        #raise IndexError('Número não encontrado')
        #return None
    if search == t[mid]:
        return mid
   
    elif search > t[mid]:
        return mid + in_bisect(t[mid:], search)

    else:
        return mid + in_bisect(t[:mid], search)
''

def in_bisect(t, search):
    chao = 0
    teto = len(t)

    while(True):
        mid = int(len(t) / 2) + chao
        print("search:", search," mid:", mid, " t:", t)

        if search == t[mid]:
            return mid
   
        elif search > t[mid]:
            chao = mid

        else:
            teto = mid
'''
def in_bisect(t, search):
    return None

t = [1,2,3,4,5,6,7,8,9,10,11,12]
search = 1

print("\n", in_bisect(t, search), end=' = ')
print(t.index(search))
