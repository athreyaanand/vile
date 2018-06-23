from Individual.Individual import Individual
from Individual.DNA import DNA

from Factories.BabyFactory import BabyFactory
from Factories.MatchFactory import MatchFactory
from Factories.NameFactory import NameFactory

from Universe.Universe import Universe


adam = Individual(DNA("00000000"), "Adam", "Pomegranate", "M", "", "", [])
eve = Individual(DNA("11111111"), "Eve", "Pomegranate", "F", "", "", [])


BabyFactory = BabyFactory()

baby_1 = BabyFactory.make(adam, eve)
baby_2 = BabyFactory.make(adam, eve)
baby_3 = BabyFactory.make(adam, eve)

baby_1.add_sibling(baby_2)
baby_1.add_sibling(baby_3)

baby_2.add_sibling(baby_3)

print("Baby 1 Siblings:", end=" ")
for sib in (baby_1.get_siblings()):
  print(sib.get_name(), end=' & ')

print("")

print("Baby 2 Siblings:", end=" ")
for sib in (baby_2.get_siblings()):
  print(sib.get_name(), end=' & ')

print("")

print("Baby 3 Siblings:", end=" ")
for sib in (baby_3.get_siblings()):
  print(sib.get_name(), end=' & ')

# print("::: DNA - CREATE :::")

# raw_a = "11111111"
# raw_b = "00000000"
# raw_c = "01010101"

# dna_a = DNA(raw_a)
# dna_b = DNA(raw_b)
# dna_c = DNA(raw_c)

# print("DNA A: " + dna_a.getDNA())
# print("DNA B: " + dna_b.getDNA())
# print("DNA C: " + dna_c.getDNA())

# print("\n::: DNA - CROSS :::")

# dna_ab = dna_a.cross(dna_b)
# dna_bc = dna_b.cross(dna_c)

# print("A x B: " + dna_a.getDNA() + " x " + dna_b.getDNA() + " >>> " + dna_ab.getDNA())
# print("B x C: " + dna_b.getDNA() + " x " + dna_c.getDNA() + " >>> " + dna_bc.getDNA())

# print("\n::: DNA - MUTATE :::")

# dna_a = dna_a.mutate()
# dna_b = dna_b.mutate()

# print("!A: " + raw_a + " >>> " + dna_a.getDNA())
# print("!B: " + raw_b + " >>> " + dna_b.getDNA())
