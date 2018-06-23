#RUN THIS
import sys
sys.path.append('Individual')
sys.path.append('Individual/Helpers')

import random

from DNA import DNA
from Person import Person
from BabyFactory import BabyFactory
from MatchFactory import MatchFactory

# Create seed people
dna_a = DNA("11111111")
dna_b = DNA("00000000")
person_a = Person(dna_a, "Eve", "F")
person_b = Person(dna_b, "Adam", "M")

print(person_a.info())
print(person_b.info())

Universe = [person_a, person_b]

BabyFactory = BabyFactory()
MatchFactory = MatchFactory(Universe)

for x in range(0,10):
  matches = MatchFactory.find_matches()
  for y in range(0, len(matches)-1):
    print("--- MATCHED: " + matches[y][0].info() + " & " + matches[y][1].info())
    baby = BabyFactory.make(matches[y][0], matches[y][1])
    Universe.append(baby)
    MatchFactory.update_universe(Universe)
