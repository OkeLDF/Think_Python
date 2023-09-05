import turtle as tt

line_len = 30

def koch(t, length):
    x = length/3
    
    if length < line_len:
        t.fd(x)
        return

    koch(t, x)
    t.lt(60)
    koch(t, x)
    t.rt(120)
    koch(t, x)
    t.lt(60)
    koch(t, x)

def cesaro(t, length):
    for i in range(4):
        koch(t, length)
        t.lt(90)

def quad_type1(t, length):
    x = length/3
    
    if length < line_len:
        t.fd(x)
        return

    quad_type1(t, x)
    t.lt(90)
    quad_type1(t, x)
    t.rt(90)
    quad_type1(t, x)
    t.rt(90)
    quad_type1(t, x)
    t.lt(90)
    quad_type1(t, x)

def quad_type2(t, length):
    x = length/3
    
    if length < line_len:
        t.fd(x)
        return

    quad_type2(t, x)
    t.lt(90)
    quad_type2(t, x)
    t.rt(90)
    quad_type2(t, x)
    t.rt(90)
    quad_type2(t, x)
    quad_type2(t, x)
    t.lt(90)
    quad_type2(t, x)
    t.lt(90)
    quad_type2(t, x)
    t.rt(90)
    quad_type2(t, x)

def minkowski(t, length):
    x = length/3

    if length < line_len:
        t.fd(x)
        return

    minkowski(t, x)
    t.lt(90)
    minkowski(t, x)
    t.rt(90)
    minkowski(t, x)
    t.rt(90)
    minkowski(t, x)
    t.lt(90)
    minkowski(t, x)
    t.rt(90)
    minkowski(t, x)
    t.lt(90)
    minkowski(t, x)
    t.lt(90)
    minkowski(t, x)
    t.rt(90)
    minkowski(t, x)

def island(t, length):
    x = length/3

    if length < line_len:
        t.fd(x)
        return

    island(t, x)
    t.lt(90)
    island(t, x)
    island(t, x)
    t.rt(90)
    island(t, x)
    island(t, x)
    t.rt(90)
    island(t, x)
    t.rt(90)
    island(t, x)
    t.lt(90)
    island(t, x)

    t.lt(90)
    island(t, x)
    island(t, x)
    t.rt(90)
    island(t, x)
    t.rt(90)
    island(t, x)
    t.lt(90)
    island(t, x)
    t.lt(90)
    island(t, x)
    island(t, x)
    t.lt(90)
    island(t, x)
    island(t, x)
    t.rt(90)
    island(t, x)

def snowflake(t, length, fractal, n):
    for i in range(n):
        fractal(t, length)
        t.rt(360/n)

bob = tt.Turtle()

bob.pu()
bob.goto(-340,0) # para o bob começar a desenhar mais à esquerda
bob.pd()

"exercício 5.6 do livro Think Python"
#koch(bob, 500)        # faz só a "curva"
#snowflake(bob, 500, koch, 3)    # faz 3 "curvas" que formam um floco

"outros fractais"
#cesaro(bob,100)
#quad_type1(bob, 500)
#quad_type2(bob, 500)
#minkowski(bob, 500)
#island(bob, 100)

snowflake(bob, 500, quad_type2, 4)

tt.mainloop()
