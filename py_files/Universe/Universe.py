from Individual.Individual import Individual
from Individual.DNA import DNA

from Factories.BabyFactory import BabyFactory
from Factories.MatchFactory import MatchFactory
#from Factories.NameFactory import NameFactory

class Universe(object):
  def __init__(self):
    self.current_tick = 0
    self.universe = []

  def spawn(self, universe):
    print(">>> UNIVERSE STARTED <<<")
    self.universe = universe
    self.BabyFactory = BabyFactory()
    self.MatchFactory = MatchFactory(self.universe)

  def run(self, ticks_long):
    for x in range(self.current_tick, self.current_tick + ticks_long):
      print("--- TICK " + str(self.current_tick) + " ---")
      self.tick()
      self.current_tick += 1
  
  def tick(self):
    matches = self.MatchFactory.find_matches()
    for x in range(0, len(matches)-1):
      #print("--- MATCHED: " + matches[x][0].info() + " & " + matches[x][1].info())
      baby = self.BabyFactory.make(matches[x][0], matches[x][1])
      self.universe.append(baby)
      self.MatchFactory.update_universe(self.universe)
      
  def end(self):
    print(">>> UNIVERSE ENDED <<<")