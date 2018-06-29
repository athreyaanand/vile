from Individual.DNA import DNA

class TraitFactory(object):

  def __init__(self):
    self.traits = ["Gender", "Height", "Weight", "Eye Color", "Skin Color"]

  # def create_DNA(self, traits):
  #   return DNA("110010")

  def create_traits(self, DNA):
    res = [None]*5
    res[0] = self.calc_gender(DNA.get_gene("Gender"))
    res[1] = self.calc_height(DNA.get_gene("Height"))
    res[2] = self.calc_weight(DNA.get_gene("Weight"))
    res[3] = self.calc_eyecolor(DNA.get_gene("Eye Color"))
    res[4] = self.calc_skincolor(DNA.get_gene("Skin Color"))

    trait_dict = {}

    for i in range(0, len(self.traits)):
      trait_dict[self.traits[i]] = res[i]

    return trait_dict

  def calc_gender(self, gene):
    return gene[2:]
  
  def calc_height(self, gene):
    return gene[2:]

  def calc_weight(self, gene):
    return gene[2:]

  def calc_eyecolor(self, gene):
    return gene[2:]

  def calc_skincolor(self, gene):
    return gene[2:]