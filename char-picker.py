# char-picker
# Emily
# 2017-02-17

import random

classes=["cleric", "fighter", "rogue", "wizard"]

#print classes[random (0,3)]

#for n in range (0, 4):
#  print classes[n]

randomizer = random.randint(0, 3)

print "Your character class is:", classes[randomizer]
