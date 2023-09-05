import turtle as tt
import math

# RESPOSTA DO LIVRO (Allen B. Downey. Think Python. p. 40-42):

'''
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)
    
def arc(t, r, a):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1 # otimização de cada traço do círculo aproximado
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)
    
def polygon(t, n, length):
    angle = 360/n
    polyline(t, n, length, angle)
'''

def arc(t, r, a):
    if a <= 0 or r <= 0:
        return

    length = 2*math.pi
    angle = 360/r
    r /= (360/a)

    for i in range(int(r)):
        t.fd(length)
        t.rt(angle)

def circle(t, r):

    if r <= 0:
        return

    polygon(t, r, 2*math.pi)

def polygon(t, n, length):

    if n <= 0:
        return

    angle = 360/n
    
    for i in range(n):
        t.fd(length)
        t.rt(angle)

bob = tt.Turtle()

bob.lt(90)
bob.fd(200)
bob.rt(90)

#polygon(bob, 3, 200)
#circle(bob, 200)
arc(bob,200,135)

tt.mainloop()
