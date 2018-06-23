import random

from DNA import DNA
from Individual import Individual
from NameFactory import NameFactory

class BabyFactory(object):
    def __init__(self):
      self.NameFactory = NameFactory()

    def make(self, parent_a, parent_b):
      dna_a = parent_a.dna
      dna_b = parent_b.dna

      dna_ab = dna_a.cross(dna_b)
      dna_ab = dna_ab.mutate()

      if random.choice([0,1]) == 0:
        sex = "M"
      else:
        sex = "F"
      
      f_name = self.NameFactory.generate_name(sex)
      l_name = self.NameFactory.generate_name(sex)

      individual = Individual(dna_ab, f_name, l_name, sex, parent_a, parent_b, [])

      print(parent_a.info() + " & " + parent_b.info() + " MADE --> " + individual.info())

      return individual