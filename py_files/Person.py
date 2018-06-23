class Person(object):
  def __init__(self, dna, name, sex):
    self.dna = dna
    self.name = name
    self.sex = sex
  def info(self):
    return self.name + " (" + self.sex + ")"
  def get_name(self):
    return self.name