# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, ...

def fibo(n):
    if n < 2:
        return n

    return fibo(n-1) + fibo(n-2)

memo = {0:0, 1:1}

def memo_fibo(n):
    if n in memo:
        return memo[n]

    memo[n] = memo_fibo(n-1) + memo_fibo(n-2)
    return memo[n]

'''
print("___ FIBONACCI RUIM ___\n")

for n in range(38):
    print("fibonacci: termo", n)
    print(fibo(n), "\n")
'''

print("\n___ FIBONACCI OTIMIZADO ___\n")

for n in range(101):
    print("fibonacci: termo", n)
    print(memo_fibo(n), "\n")
