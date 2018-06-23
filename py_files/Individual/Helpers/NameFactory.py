import random

class NameFactory(object):

  def __init__(self):
  self.vowels = ["a"] * 50 + ["e"] * 50 + ["i"] * 50 + ["o"] * 50 + ["u"] * 50 + ["y"] * 10 + ["oe"] * 15 + ["ee"] * 15 + ["oo"] * 15
  self.consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "ph", "th", "ck", "ch", "ng", "tr", "sh"] 
  self.lengths = ['3'] * 25 + ['4'] * 194 + ['5'] * 277 + ['6'] * 308 + ['7'] * 85 + ['8'] * 15 + ['9'] * 7 + ['10'] * 5

  def generate_name(self, gender):
    namelength = random.choice(self.lengths)
    name = ""

    for x in range (int(namelength)):
      if x%2 == 0:
        name += self.consonants[random.randint(0, len(self.consonants)-1)]
      else:
        name += self.vowels[random.randint(0, len(self.vowels)-1)]
    
    if str(gender) is "F" and random.randint(0, 100) < 90 and int(namelength)%2 != 1:
      name += self.vowels[random.randint(0, len(self.vowels)-1)]
    
    if (str(gender) == "F") and (random.randint(0, 100) < 90):
      name = name[1:]
    
    avg_length +=  len(name)
    return name.capitalize()

#TESTBLOCK__________________________________________________
#  print gender + " -- " + name

#for x in range(100):
#  if x < 50:
#    generate_name("F")
#  else:
#    generate_name("M")
#
#print ("THE AVERAGE NAME LENGTH IS: " + str(avg_length/100))