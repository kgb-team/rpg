
from Charactersystem import Character
from ClientNetwork import NetworkConnector

#network = NetworkConnector()
#network.sendmessage(input("Message: "))
#while True:
#  msg = network.receivemessage()
#  print(msg)

#Funktion zum zuweisen der Attribute zu einer Zahl
def print_list(attr_list):
  for i, val in enumerate(attr_list):
    print("%s:" %i, val)
    
def print_dictkeys(attr_dict):
  for i, val in attr_dict.items():
    print(i)
    
#Zuweisung desObjekts zur Blaupause
playerObj = Newcharacter()

#Optionen der einzelnen Werte für die Keys des look und attributes dictionary
playerObj.name = input("Name:")
print(playerObj.name)

print("Wähle eine Rasse:")
print_list(playerObj.available["races"])
playerObj.attributes["race"] = int(input("Rasse:"))

print("Wähle eine Rolle:")
print_list(playerObj.available["roles"])
playerObj.attributes["role"] = int(input("Rolle:"))

print("Wähle Zugehörigkeit:")
print_list(playerObj.available["affinity"])
playerObj.attributes["affinity"] = int(input("Zugehörigkeit:"))

print("Wähle eine Haarfarbe:")
print_list(playerObj.available["haircolors"])
playerObj.look["haircolor"] = int(input("Haarfarbe: "))

print("Wähle eine Haarlänge:")
print_list(playerObj.available["hairlengths"])
playerObj.look["hairlength"] = int(input("Haarlänge: "))

print("Wähle eine Augenfarbe:")
print_list(playerObj.available["eyecolors"])
playerObj.look["eyecolor"] = int(input("Augenfarbe: "))

print("Wähle einen Körperbau:")
print_list(playerObj.available["bodystructures"])
playerObj.look["bodystructure"] = int(input("Körperbau: "))

print("Wähle Gegenstände:")
playerObj.items = input("Gegenstände:").split(",")
playerObj.numbers = list(map(int, input("Anzahlen:").split(",")))
playerObj.inventory = dict(zip(playerObj.items, playerObj.numbers))

playerObj.calc_stats(playerObj.available["racestats"][playerObj.attributes["race"]], playerObj.available["rolestats"][playerObj.attributes["role"]])

print(playerObj.look)
print(playerObj.attributes)
print(playerObj.inventory)
