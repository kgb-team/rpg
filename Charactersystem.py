class Newcharacter():
  def __init__(self):
    self.available = {}
    self.available["races"] = ["Kandri", "Menschen", "Zwerge", "Orks"]
    self.available["roles"] = ["Paladin", "Schurke", "Magier", "Krieger", "Priester", "Jäger", "Druide"]
    self.available["haircolors"] = ["schwarz", "braun", "blond", "rot"]
    self.available["hairlengths"] = ["lang", "mittel", "kurz"]
    self.available["eyecolors"] = ["schwarz", "blau", "grün", "rot", "weiß", "braun"]
    self.available["bodystructures"] = ["dünn", "dick", "muskulös", "drahtig"]
    
    self.name = ""
    self.look = {}
    self.attributes = {}
    self.inventory = {}
    self.items = None
    self.numbers = None

