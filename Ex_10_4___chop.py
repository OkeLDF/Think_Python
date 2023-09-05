def chop(t):
    t.pop(0)
    t.pop(len(t)-1)

t = [1, 2, 3, 4]
print(chop(t))
print(t)
