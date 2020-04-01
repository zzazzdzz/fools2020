import random

slots = [0,0,0,0,0,0,0]

while 1:
    slot = random.choice((0,1,2,3,4,5,6))
    it = random.choice((1,2,3,4))
    slots[slot] = it
    print(slots)
    if 1 in slots and 2 in slots and 3 in slots and 4 in slots:
        break