#Blaupause zum erstellen von Charaktere
class Newcharacter():
  #Funktion, die alles beim zuweisen zu einem Objekt einmal ausführt
  def __init__(self):
    self.available = {}
    self.available["racestats"] = [{"Hpbase":100, "Attackbase":50, "Defensebase":20, "Abilitypowerbase":60, "Magicdefensebase":30},
                                  {"Hpbase":150, "Attackbase":30, "Defensebase":30, "Abilitypowerbase":30, "Magicdefensebase":30},
                                  {"Hpbase":150, "Attackbase":40, "Defensebase":50, "Abilitypowerbase":20, "Magicdefensebase":20},
                                  {"Hpbase":170, "Attackbase":40, "Defensebase":60, "Abilitypowerbase":10, "Magicdefensebase":10}]
    self.available["races"] = ["Kandri", "Menschen", "Zwerge", "Orks"]
    self.available["rolestats"] = [{"Hpbase":1, "Attackbase":1.5, "Defensebase":1.5, "Abilitypowerbase":0.5, "Magicdefensebase":0.5},
                                  {"Hpbase":0.75, "Attackbase":2, "Defensebase":0.75, "Abilitypowerbase":1, "Magicdefensebase":1},
                                  {"Hpbase":0.75, "Attackbase":0.75, "Defensebase":0.5, "Abilitypowerbase":2, "Magicdefensebase":2},
                                  {"Hpbase":1.5, "Attackbase":1.5, "Defensebase":1.5, "Abilitypowerbase":0.5, "Magicdefensebase":0.5},
                                  {"Hpbase":1, "Attackbase":1, "Defensebase":1.5, "Abilitypowerbase":1.5, "Magicdefensebase":1.5},
                                  {"Hpbase":1, "Attackbase":2, "Defensebase":0.5, "Abilitypowerbase":0.5, "Magicdefensebase":1.5},
                                  {"Hpbase":1, "Attackbase":1, "Defensebase":1, "Abilitypowerbase":1.5, "Magicdefensebase":1.5}]
    self.available["roles"] = ["Paladin", "Schurke", "Magier", "Krieger", "Priester", "Jäger", "Druide"]
    self.available["affinity"] = {"Gegner", "Verbündeter", "Gesteuerter Verbündeter"}
    self.available["haircolors"] = {"schwarz", "braun", "blond", "rot"}
    self.available["hairlengths"] = {"lang", "mittel", "kurz"}
    self.available["eyecolors"] = {"schwarz", "blau", "grün", "rot", "weiß", "braun"}
    self.available["bodystructures"] = {"dünn", "dick", "muskulös", "drahtig"}
    self.name = ""
    self.look = {}
    self.attributes = {}
    self.inventory = {}
    self.items = None
    self.numbers = None

  def calc_stats(self, racestat, rolestat):
    self.statsset = {"Hpbase": racestat["Hpbase"] * rolestat["Hpbase"],
                    "Attackbase": racestat["Attackbase"] * rolestat["Attackbase"],
                    "Defensebase": racestat["Defensebase"] * rolestat["Defensebase"],
                    "Abilitypowerbase": racestat["Abilitypowerbase"] * rolestat["Abilitypowerbase"],
                    "Magicdefensebase": racestat["Magicdefensebase"] * rolestat["Magicdefensebase"]}
    print(self.statsset)