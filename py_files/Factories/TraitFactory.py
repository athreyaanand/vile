# Returns an array of traits, given DNA
# OR creates DNA from given traits

import webcolors

from Individual.DNA import DNA

class TraitFactory(object):

  def __init__(self):
    self.zero = 0

  # def create_DNA(self, traits):
  #   return DNA("110010")

  def create_traits(self, Individual):
    self.dna = Individual.dna
    return self.calc_color()
  
  def calc_color(self):
    segment = self.dna.getDNA() # pick a seg
    #color = hex(int(segment, 2))
    color = hex(int(segment, 2))
    print(color)
    ff = self.hex_to_rgb(color)
    print("val: " + str(ff))
    result = self.get_colour_name(ff)

    print(result)
    return result
    #return self.get_colour_name(aa)
    #return self.hex_to_rgb(color)
    #return self.get_colour_name(self.closest_color(self.hex_to_rgb(color)))

  def hex_to_rgb(self, value):
    value = value.lstrip('0x')
    return tuple(int(value[i:i+1], 16) for i in range(0, 3, 1))
    
  def closest_colour(self, requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        print(key + " " + name)
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

  def get_colour_name(self, requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = self.closest_colour(requested_colour)
        actual_name = None
    return closest_name
