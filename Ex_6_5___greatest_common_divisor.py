def gcd(a, b):
    if b == 0:
        return a
        
    elif a>b:
        return gcd(b, a%b)

    elif b>a:
        return gcd(a, b%a)

x = int(input("give the x value: "))
y = int(input("give the y value: "))

print("the gcd of %i and %i is:"%(x,y), gcd(x,y))
