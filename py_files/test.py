from Individual.Individual import Individual
from Individual.DNA import DNA

from Factories.BabyFactory import BabyFactory
from Factories.MatchFactory import MatchFactory
from Factories.NameFactory import NameFactory

from Universe.Universe import Universe


adam = Individual(DNA("00000000"), "Adam", "Pomegranate", "M", "", "", [])
eve = Individual(DNA("11111111"), "Eve", "Watermelon", "F", "", "", [])

adam.marry(eve)

if(adam.lastname == eve.lastname): print("Names Match! - " + adam.lastname + " & " + eve.lastname)
else: print("FAIL! - " + adam.lastname + " & " + eve.lastname)


print(adam.name + "'s Spouse: " + adam.spouse.name)
print(eve.name + "'s Spouse: " + eve.spouse.name)

BabyFactory = BabyFactory()

baby_1 = BabyFactory.make(adam, eve)
baby_2 = BabyFactory.make(adam, eve)
baby_3 = BabyFactory.make(adam, eve)

baby_1.add_sibling(baby_2)
baby_1.add_sibling(baby_3)

baby_2.add_sibling(baby_3)

print("Baby 1 Siblings:", end=" ")
for sib in baby_1.siblings:
  print(sib.name, end=' & ')

print("")

print("Baby 2 Siblings:", end=" ")
for sib in baby_2.siblings:
  print(sib.name, end=' & ')

print("")

print("Baby 3 Siblings:", end=" ")
for sib in baby_3.siblings:
  print(sib.name, end=' & ')

print("")
print("Baby 1 Parents: " + baby_1.father.name + " (Father) & " + baby_1.mother.name + " (Mother)")
print("Baby 2 Parents: " + baby_2.father.name + " (Father) & " + baby_2.mother.name + " (Mother)")
print("Baby 3 Parents: " + baby_3.father.name + " (Father) & " + baby_3.mother.name + " (Mother)")

print("::: DNA - CREATE :::")

raw_a = "11111111"
raw_b = "00000000"
raw_c = "01010101"

dna_a = DNA(raw_a)
dna_b = DNA(raw_b)
dna_c = DNA(raw_c)

print("DNA A: " + dna_a.dna)
print("DNA B: " + dna_b.dna)
print("DNA C: " + dna_c.dna)

print("\n::: DNA - CROSS :::")

dna_ab = dna_a.cross(dna_b)
dna_bc = dna_b.cross(dna_c)

print("A x B: " + dna_a.dna + " x " + dna_b.dna + " >>> " + dna_ab.dna)
print("B x C: " + dna_b.dna + " x " + dna_c.dna + " >>> " + dna_bc.dna)

print("\n::: DNA - MUTATE :::")

dna_a = dna_a.mutate()
dna_b = dna_b.mutate()

print("!A: " + raw_a + " >>> " + dna_a.dna)
print("!B: " + raw_b + " >>> " + dna_b.dna)