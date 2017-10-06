from rubik import cube
from copy import deepcopy
import random
import time


madict = {"patata":"i'm a patata"}


def test(thing):
    try:
        holder = madict[thing]
        print("FULL", madict[thing])
    except KeyError:
        print("EMPTY")
