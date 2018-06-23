class Universe(object):
  def __init__(self):
    self.tick = 0

  def spawn(self, universe):
    print("UNIVERSE STARTED")
    self.universe = universe

  def run(self, ticks_long):
    for x in range(self.tick, self.tick + ticks_long):
      print("--- TICK " + str(self.tick) + " ---")
      self.tick += 1
      
  def end(self):
    print("UNIVERSE ENDED")