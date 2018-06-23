from Universe.Universe import Universe

from Individual.Individual import Individual
from Individual.DNA import DNA

universe = Universe()

adam = Individual(DNA("11110000"), "Eve", "GOD", "F", "GOD", "GOD", [])
eve = Individual(DNA("00001111"), "Adam", "GOD", "M", "GOD", "GOD", [])
seed = [adam, eve]

universe.spawn(seed)

universe.run(10)
universe.run(3)
universe.run(2)

universe.end()