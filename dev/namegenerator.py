import random

vowels = ["a"] * 50 + ["e"] * 50 + ["i"] * 50 + ["o"] * 50 + ["u"] * 50 + ["y"] * 10 + ["oe"] * 15 + ["ee"] * 15 + ["oo"] * 15
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "ph", "th", "ck", "ch", "ng", "tr", "sh"] 
lengths = ['3'] * 25 + ['4'] * 194 + ['5'] * 277 + ['6'] * 308 + ['7'] * 85 + ['8'] * 15 + ['9'] * 7 + ['10'] * 5

avg_length = 0.0

def generate_name(gender):
  global avg_length

  namelength = random.choice(lengths)
  name = ""
  for x in range (int(namelength)):
    if x%2 == 0:
      name += consonants[random.randint(0, len(consonants)-1)]
    else:
      name += vowels[random.randint(0, len(vowels)-1)]
  
  if str(gender) is "F" and random.randint(0, 100) < 90 and int(namelength)%2 != 1:
    name += vowels[random.randint(0, len(vowels)-1)]
  
  if (str(gender) == "F") and (random.randint(0, 100) < 90):
    name = name[1:]
  
  avg_length +=  len(name)
  print gender + " -- " + name

for x in range(100):
  if x < 50:
    generate_name("F")
  else:
    generate_name("M")

print ("THE AVERAGE NAME LENGTH IS: " + str(avg_length/100))

