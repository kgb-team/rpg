
#Blaupause zum erstellen von Charaktere
class Character():
  #Funktion, die alles beim zuweisen zu einem Objekt einmal ausführt
  available = {}
  characters = []
  maxxp = self.level
  available["racestats"] = [{"Hpbase":100, "Attackbase":50, "Defensebase":20, "Abilitypowerbase":60, "Magicdefensebase":30},
                            {"Hpbase":150, "Attackbase":30, "Defensebase":30, "Abilitypowerbase":30, "Magicdefensebase":30},
                            {"Hpbase":150, "Attackbase":40, "Defensebase":50, "Abilitypowerbase":20, "Magicdefensebase":20},
                            {"Hpbase":170, "Attackbase":40, "Defensebase":60, "Abilitypowerbase":10, "Magicdefensebase":10}]
  available["races"] = ["Kandri", "Menschen", "Zwerge", "Orks"]
  available["rolestats"] = [{"Hpbase":1, "Attackbase":1.5, "Defensebase":1.5, "Abilitypowerbase":0.5, "Magicdefensebase":0.5},
                            {"Hpbase":0.75, "Attackbase":2, "Defensebase":0.75, "Abilitypowerbase":1, "Magicdefensebase":1},
                            {"Hpbase":0.75, "Attackbase":0.75, "Defensebase":0.5, "Abilitypowerbase":2, "Magicdefensebase":2},
                            {"Hpbase":1.5, "Attackbase":1.5, "Defensebase":1.5, "Abilitypowerbase":0.5, "Magicdefensebase":0.5},
                            {"Hpbase":1, "Attackbase":2, "Defensebase":0.5, "Abilitypowerbase":0.5, "Magicdefensebase":1.5},
                            {"Hpbase":1, "Attackbase":1, "Defensebase":1, "Abilitypowerbase":1.5, "Magicdefensebase":1.5}]
  available["roles"] = ["Paladin", "Schurke", "Magier", "Krieger", "Jäger", "Druide"]
  available["affinity"] = ["Gegner", "Verbündeter", "Gesteuerter Verbündeter"]
  available["haircolors"] = ["schwarz", "braun", "blond", "rot"]
  available["hairlengths"] = ["lang", "mittel", "kurz"]
  available["eyecolors"] = ["schwarz", "blau", "grün", "rot", "weiß", "braun"]
  available["bodystructures"] = ["dünn", "dick", "muskulös", "drahtig"]
  
  def __init__(self):
    self.name = ""
    self.look = {}
    self.attributes = {}
    self.inventory = {}
    self.items = None
    self.numbers = None

  def calc_stats(self, racestat, rolestat):
    self.basestatsset = {"Hpbase": racestat["Hpbase"] * rolestat["Hpbase"],
                    "Attackbase": racestat["Attackbase"] * rolestat["Attackbase"],
                    "Defensebase": racestat["Defensebase"] * rolestat["Defensebase"],
                    "Abilitypowerbase": racestat["Abilitypowerbase"] * rolestat["Abilitypowerbase"],
                    "Magicdefensebase": racestat["Magicdefensebase"] * rolestat["Magicdefensebase"]}
  
  def character(self):
    self.character = [self.name, self.look, self.attributes, self.inventory]
    characters.append(self.character) 
  
  def objxp(self):
    self.gainedxp = 
    self.excessxp = self.gainedxp-maxxp
  
  def objlevel(self):
    self.level = 0
    self.maxlevel = 100
    if self.gainedxp >= maxxp:
      self.level = self.level+1
      self.xp = self.excessxp
  
  def stats(self):
    self.statsset = {"Hp":self.basestatsset["Hpbase"]+self.level*5, "Attack":self.basestatsset["Attackbase"]+self.level*5,\
    "Defense":self.basestatsset["Defensebase"]+self.level*5, "Abilitypower":self.basestatsset["Abilitypowerbase"]+self.level*5,\
    "Magicdefense":self.basestatsset["Magicdefensebase"]+self.level*5,}    

  
      
      
    
    
  
  
 
  