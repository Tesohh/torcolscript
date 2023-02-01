# TorcolScript
# Scritto da tesohh e alder (p1)

from tParser import log, torcler
from pprinter import pprint
import sys

try:
    if len(sys.argv) > 1:
        fileToOpen = sys.argv[1]
    else:
        print("""\033[94m
█████████████████████████████████
█████████████████████████████████
█████████████████████████████████\033[0m
█████████████████████████████████
█████████████████████████████████
█████████████████████████████████\033[92m
█████████████████████████████████
█████████████████████████████████
█████████████████████████████████
\033[0m""")
        fileToOpen = "nop.torcol"
    f = open(fileToOpen, "r")
except:
    log(f"Sto ciapin {fileToOpen} no le stat troà", 2)
    exit()

torcol = f.read()
f.close()

try:
    if sys.argv[2] == "cat":
        pprint(torcol)
        quit()
except IndexError:
    pass

torcler(torcol)
