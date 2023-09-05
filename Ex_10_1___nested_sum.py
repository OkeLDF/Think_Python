def nested_sum(lista):
    ' t: int list '
    total = 0

    for elem in lista:
        if isinstance(elem, list):
            total += nested_sum(elem)

        elif isinstance(elem, (int, float)):
            total += elem
    
    return total

t = [[1,2],[3],[4,5,[6]]]
print(nested_sum(t))

t = []
print(nested_sum(t))

t = [[],[['a'],[8.5]]]
print(nested_sum(t))
