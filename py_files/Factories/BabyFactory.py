import random

from Individual.DNA import DNA
from Individual.Individual import Individual
from Factories.NameFactory import NameFactory

class BabyFactory(object):
    def __init__(self):
      self.NameFactory = NameFactory()

    def make(self, father, mother):
      dna_a = father.dna
      dna_b = mother.dna

      dna_ab = dna_a.cross(dna_b)
      dna_ab = dna_ab.mutate()

      sex = random.choice(["M", "F"])
      
      f_name = self.NameFactory.generate_name(sex)
      l_name = self.NameFactory.generate_name(sex)

      individual = Individual(dna_ab, f_name, father.lastname, sex, father, mother, [])

      print(father.info() + " & " + mother.info() + " MADE --> " + individual.info())

      return individual
