from Factories.TraitFactory import TraitFactory
from Individual.DNA import DNA
from Individual.Individual import Individual

TraitFactory = TraitFactory()

adam = Individual(DNA("010111011100"), "Eve", "GOD", "F", "GOD", "GOD", [])

res = TraitFactory.create_traits(adam)
print("Color: " + res)

