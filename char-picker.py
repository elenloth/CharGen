# char-picker
# Emily
# 2017-02-17

import random

classes=["cleric", "fighter", "rogue", "wizard"]
races=["dwarf", "elf", "halfling", "human"]
abil=["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

print "####################\nCharacter Generator\n####################"

randomizer = random.randint(0, 3)
print "Your character class is:", classes[randomizer]

randomizer = random.randint(0,3)
print "Your character race is:", races[randomizer] 


for n in abil:
  ability = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
  print "Your", n, "is:", ability



