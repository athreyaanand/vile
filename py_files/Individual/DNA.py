import random

class DNA(object):

  def __init__(self, dna):
    self.dna = dna
    self.MUTATE_RATE = .125
    self.genes = dna.split(':')
    self.traits = ["Gender", "Height", "Weight", "Eye Color", "Skin Color"]

  def get_gene(self, trait):
    return self.genes[self.traits.index(trait)]

  def cross(self, otherDNA):
    #for now just choose 1 bit from either parent, later deal with sectons
    dna_new = ""
    dna_a = list(self.dna)
    dna_b = list(otherDNA.dna)

    for x in range(len(dna_a)):
      if random.choice([0,1]) == 0:
        dna_new += dna_a[x]
        #print("Pick A " + dna_a[x])
      else:
        dna_new += dna_b[x]
        #print("Pick B " + dna_b[x])
    return DNA(dna_new)

  def mutate(self):
    #print("DNA B4 MUTATE: " + self.dna)
    dna_arr = list(self.dna)
    for x in range(len(dna_arr)):
      if random.uniform(0,1) > (1-self.MUTATE_RATE):
        #print(">>>> MUTATING @x=" + str(x))
        dna_arr[x] = str((int(dna_arr[x]) + 1) % 2)
    return DNA("".join(dna_arr))