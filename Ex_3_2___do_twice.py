def print_s(s):
    print(s)
    
def do_twice(f, s):
    f(s)
    f(s)

def do_four(f, s):
    do_twice(f, s)
    do_twice(f, s)

def draw_squares():
    print("+", end='')
    do_four(print, "-")
    print("+", end='')
    do_four(print, "-")
    print("+", end='')

do_twice(print_s, "Hello World")
print()
do_four(print_s, "The knights who say 'ni'!")
print()
draw_squares()
