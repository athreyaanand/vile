#RUN THIS
import sys
sys.path.append('Individual')
sys.path.append('Individual/Helpers')

import random

from DNA import DNA
from Individual import Individual
from BabyFactory import BabyFactory
from MatchFactory import MatchFactory

# Create seed people
dna_a = DNA("11110000")
dna_b = DNA("00001111")
adam = Individual(dna_a, "Eve", "GOD", "F", "GOD", "GOD", [])
eve = Individual(dna_a, "Adam", "GOD", "M", "GOD", "GOD", [])

print(adam.info())
print(eve.info())

Universe = [adam, eve]

BabyFactory = BabyFactory()
MatchFactory = MatchFactory(Universe)

for x in range(0,10):
  matches = MatchFactory.find_matches()
  for y in range(0, len(matches)-1):
    print("--- MATCHED: " + matches[y][0].info() + " & " + matches[y][1].info())
    baby = BabyFactory.make(matches[y][0], matches[y][1])
    Universe.append(baby)
    MatchFactory.update_universe(Universe)
