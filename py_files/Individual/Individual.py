import name_generator

class Individual:
  firstname = ""
  lastname = ""
  gender = ""
  spouse = ""
  father = "god"
  mother = "god"
  children = []
  siblings = []
  name = firstname + " " + lastname
  dna = ""
  
  def __init__(self, dna, firstname, lastname, gender, father, mother, siblings):
    self.dna = dna
    if isinstance(firstname, str):
      self.firstname = firstname
    if isinstance(lastname, str):
      self.lastname = lastname
    if isinstance(gender, str):
      self.gender = gender
    if isinstance(father, Individual):
      self.father = father
    if isinstance(mother, Individual):
      self.mother = mother
    if isinstance(siblings, list):
      self.siblings = siblings

  def add_sibling(self, sibling):
    if isinstance(sibling, Individual):
      self.siblings.append(sibling)
      sibling.siblings.append(self)
  
  def marry(self, partner):
    if isinstance(partner, Individual):
      self.spouse = partner
      partner.spouse = self
      if partner.gender == "F":
        partner.lastname = self.lastname
      else:
        self.lastname = partner.lastname
  
  def info(self):
    return self.firstname + " " + self.lastname + " (" + self.gender + ")"
  
# athreya = Individual(name_generator.generate_name("F"), 
#                      name_generator.generate_name("M"), 
#                      "F",
#                      "god", 
#                      "god", 
#                      [])
# aman = Individual(name_generator.generate_name("M"), 
#                      name_generator.generate_name("M"), 
#                      "M",
#                      "god", 
#                      "god", 
#                      [])
# joseph = Individual(name_generator.generate_name("F"), 
#                      name_generator.generate_name("M"), 
#                      "F",
#                      aman, 
#                      athreya, 
#                      [])

# print athreya.name + " is married to " + aman.name
# print joseph.name + "'s parents are " + joseph.father.name + " " + joseph.mother.name
# athreya.marry(aman)
# print athreya.lastname
# print aman.lastname