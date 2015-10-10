class Newcharacter():
  def __init__(self):
    self.available = {}
    self.available["roles"] = ["Paladin", "Schurke", "Magier", "Krieger", "Priester", "Jäger", "Hexenmeister"]
    self.available["haircolors"] = ["schwarz", "braun", "blond", "rot"]
    self.available["hairlengths"] = ["lang", "mittel", "kurz"]
    self.available["eyecolors"] = ["schwarz", "blau", "grün", "rot", "weiß", "braun"]
    self.available["bodystructures"] = ["dünn", "dick", "muskulös", "drahtig"]
    
    self.name = ""
    self.look = {}
    self.role = None
    self.attributes = {"Hp": 0, "Attack": 0, "Ability Power": 0, "Defense": 0, "Magic Defense": 0}
    self.inventory = {}