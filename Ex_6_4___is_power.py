def is_divisible(a, b):
    return a%b == 0

def is_power(a, b):
    if a == 1:
        return True

    else:
        return is_divisible(a, b) and is_power(a/b, b)

x = int(input("give the x value: "))
y = int(input("give the y value: "))

print("%i is power of %i:"%(x,y), is_power(x,y))
