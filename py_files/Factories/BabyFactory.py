import random

from Individual.DNA import DNA
from Individual.Individual import Individual
from Factories.NameFactory import NameFactory

class BabyFactory(object):
    def __init__(self):
      self.NameFactory = NameFactory()

    def make(self, parent_a, parent_b):
      dna_a = parent_a.dna
      dna_b = parent_b.dna

      dna_ab = dna_a.cross(dna_b)
      dna_ab = dna_ab.mutate()

      sex = random.choice(["M", "F"])
      
      f_name = self.NameFactory.generate_name(sex)
      l_name = self.NameFactory.generate_name(sex)

      individual = Individual(dna_ab, f_name, l_name, sex, parent_a, parent_b, [])

      print(parent_a.info() + " & " + parent_b.info() + " MADE --> " + individual.info())

      return individual