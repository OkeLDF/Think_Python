import math

def factorial(n):
    if n == 0:
        return 1
    return n * (factorial(n-1))

def term_summ(k):
    return factorial(4*k) *(1103 + 26390 * k) / ((factorial(k))**4 * 396**(4*k))

def extimate_pi():
    total = 0
    fk = 0
    k = 0
    constant = ((2 * math.sqrt(2)) / 9801)
    
    while True:
        fk = constant * term_summ(k)
        total += fk

        if abs(fk) < 1e-15:
            return 1/total

        k += 1
    
print(extimate_pi())
print(math.pi)
