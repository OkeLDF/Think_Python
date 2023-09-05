def is_sorted(t):
    ver = t[:]
    ver.sort()
    return t == ver

a = [1, 2, 3, 4]
b = ['c', 'b', 'a']
c = [[3], [2, 4]]

print(is_sorted(a))
print(is_sorted(b))

print(is_sorted(c)) # kinda sus
c.sort()
print(c)
