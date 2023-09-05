import turtle as tt
import math

def petal(t, r, a):
    """
    desenha dois arcos de raio r e ângulo a com a turtle t;
    a rotação à direita serve para que t saia do ponto de origem
    e a ele retorne.
    """
    if a < 180:
        arc(t, r, a)
        t.rt(180-a)
        arc(t, r, a)

def flower(t, r, a, n):
    """
    desenha uma flor de n pétalas, sendo cada pétala um
    arco de ângulo e raio r, com a turtle t
    """
    for i in range(n):
        petal(t, r, a)
        t.lt(a+180+(360/n))

def arc(t, r, a):
    if a <= 0 or r <= 0:
        return

    length = 2*math.pi
    angle = 360/r
    r /= (360/a)

    for i in range(int(r)):
        t.fd(length)
        t.rt(angle)

bob = tt.Turtle()

flower(bob, 100, 45, 5)
arc(bob, 100, 90)
bob.lt(170)
petal(bob, 70, 60)
bob.rt(90)
petal(bob, 70, 60)

tt.mainloop()
