import turtle as tt
import math

def polygon(t, n, length):

    if n <= 0:
        return

    angle = 360/n
    
    for i in range(n):
        t.fd(length)
        t.rt(angle)

def pie(t, n, length):

    if n <= 0:
        return

    ext_ang = 360/n
    int_ang = 180 - ext_ang
    
    rot = ext_ang/2 + 90
    d = length / (2 * math.cos(math.pi/180*int_ang/2))
    #print(ext_ang, int_ang, rot, d)
    
    for i in range(n):
        t.fd(length)
        t.rt(rot)
        
        t.fd(d)
        t.rt(180)
        
        t.fd(d)
        t.rt(rot)

bob = tt.Turtle()

'''
num = int(input("Digite um número natural: "))

if num<=0:
    print("Inválido")

else:
    pie(bob, num, 100)
'''
pie(bob, 3, 100)

tt.mainloop()
