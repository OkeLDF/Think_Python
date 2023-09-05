def nested_sum(lista):
    ' t: int list '
    total = 0

    for elem in lista:
        if isinstance(elem, list):
            total += nested_sum(elem)

        elif isinstance(elem, int):
            total += elem
    
    return total

def cumsum(lista):
    ' lista: int list '
    cumulat = 0
    res = []
    
    for elem in lista:
        
        if isinstance(elem, list):
            cumulat += nested_sum(elem)
            
        elif isinstance(elem, (int, float)):
            cumulat += elem

        else:
            continue
        
        res.append(cumulat)

    return res

t = [1, 2, 3, 4]
print(cumsum(t))

t = []
print(cumsum(t))

t = [1, [2, 3, [4]], 5]
print(cumsum(t))

t = [1, 2, 'a', 4.2]
print(cumsum(t))

