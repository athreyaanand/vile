#RUN THIS

import random

from DNA import DNA
from Person import Person
from BabyFactory import BabyFactory
from MatchMaker import MatchMaker

# Create seed people
dna_a = DNA("11111111")
dna_b = DNA("00000000")
person_a = Person(dna_a, "Eve", "F")
person_b = Person(dna_b, "Adam", "M")

print(person_a.info())
print(person_b.info())

UNIVERSE = [person_a, person_b]

BabyFactory = BabyFactory()
MatchMaker = MatchMaker(UNIVERSE)

for x in range(0,10):
  matches = MatchMaker.find_matches()
  for y in range(0, len(matches)-1):
    print("--- MATCHED: " + matches[y][0].info() + " & " + matches[y][1].info())
    baby = BabyFactory.make(matches[y][0], matches[y][1])
    UNIVERSE.append(baby)
    MatchMaker.update_universe(UNIVERSE)
