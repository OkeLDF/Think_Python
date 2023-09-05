import turtle as tt

bob = tt.Turtle() # gera o bob
print(bob)

bob.fd(100) # fd == foward
bob.lt(90) # lt == left turn
bob.fd(100)

bob.pu() # pu == pen up

bob.lt(45) # rt == right turn
bob.fd(100)

bob.pd() # pd == pen down
bob.lt(45)
bob.fd(200)

bob.pu()
bob.lt(90)
bob.fd(150)
bob.pd()
for i in range(4):
    bob.lt(90)
    bob.fd(100)

tt.mainloop() # inicia o loop
