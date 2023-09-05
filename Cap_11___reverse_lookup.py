def reverse_lookup(d, v, all_occurrences=False):
    '''
    if all_occurrences is True, it returns all the
    keys in dictionary d that map to v. Otherwise,
    it returns only the first occurrence.
    '''
    keys = []
    for k in d:
        if d[k] == v:
            if not all_occurrences:
                return k
            else:
                keys.append(k)
    if keys == []:
        raise LookupError('this value does not appear in the dictionary')
    return keys

d = {'José': 1, "Francisco": 3, "Macedo": 4, "Sérgio": 1}
v = 1

print(reverse_lookup(d, v))
print(reverse_lookup(d, v, True))
#print(reverse_lookup(d, 2)) # vai dar erro
