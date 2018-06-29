from Factories.TraitFactory import TraitFactory
from Individual.DNA import DNA

TraitFactory = TraitFactory()

dnas = [None]*5
dnas[0] = DNA("1-9923:2-3243:1-5323:3-6341:2-1203")
dnas[1] = DNA("1-7293:2-6198:1-1102:3-2042:2-2212")
dnas[2] = DNA("1-2938:2-0162:1-1820:3-6623:2-1204")
dnas[3] = DNA("1-1792:2-3243:1-3384:3-4027:2-0411")
dnas[4] = DNA("1-8002:2-5142:1-0032:3-9000:2-1922")

for i in range(0, len(dnas)):
  traits = TraitFactory.create_traits(dnas[i])
  print("DNA " + str(i) + ": ", end="")
  for key in traits:
    print (key + ": " + traits[key], end=", ")
  print()