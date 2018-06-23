import random

from DNA import DNA
from Person import Person
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
      
      name = self.NameFactory.generate_name(sex)

      person = Person(dna_ab, name, sex)

      print(parent_a.info() + " & " + parent_b.info() + " MADE --> " + person.info())

      return person