from tParser import torcler

f = open("main.torcol", "r")
torcol = f.read()
f.close()

torcler(torcol)
