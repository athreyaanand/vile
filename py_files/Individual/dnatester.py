traits = ["Gender", "Height", "Weight", "EColor", "SColor"]
dna = "1-23425:2-3243:1-5323:3-6341:2-1203"

dnaarr = dna.split(':')

for i in range(0, len(traits)):
  print(traits[i] + "\n  - " + dnaarr[i].split("-")[0] + "\n  - " + dnaarr[i].split("-")[1])
