import time

t = time.time()
s = t%60

t = t//60
m = t%60

t = t//60
h = t%24

t = t//24

print("o horário do GMT é:")
print("    %i:%i:%i"%(h,m,s))

print("\njá se passaram", t, "dias desde a 'epoch'")
