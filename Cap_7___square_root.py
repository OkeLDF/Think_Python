import math

def sqrt(a):
    y = 0
    n = 1

    if a%2 == 0:
        x = a/2
    else:
        x = (a+1)/2
    
    while True:
        print(n)
        
        y = (x + a/x) / 2
        if x == y:
            return y
        
        x = y
        n += 1

a = int(input("Digite o valor do radicando: "))

print(sqrt(a))
print(math.sqrt(a))
