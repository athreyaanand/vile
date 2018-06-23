import random

class MatchMaker(object):
  def __init__(self, universe):
    self.universe = universe

  def find_matches(self):
    #find all matchees
    # for now start w/ 2
    matches = []
    for x in range(0,3):
      matchee = self.universe[random.randint(0, len(self.universe)-1)]
      match = self.find_match(matchee)
      matches.append([matchee, match])
      #print("MATCHED: " + matchee.info() + " & " + match.info())

    return matches

  def find_match(self, matchee):
    # Finds a random match (will replace with more params)
    match = self.universe[random.randint(0, len(self.universe)-1)]

    return match

  def update_universe(self, universe):
    self.universe = universe