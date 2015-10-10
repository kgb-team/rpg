from Charactersystem import Newcharacter

def print_list(attr_list):
  for i, val in enumerate(attr_list):
    print("%s:" %i, val)

playerObj = Newcharacter()

playerObj.name = input("Name:")
print(playerObj.name)

print("Wähle eine Rasse:")
print_list(playerObj.available["races"])
playerObj.attributes["race"] = int(input("Rasse:"))

print("Wähle eine Rolle:")
print_list(playerObj.available["roles"])
playerObj.attributes["role"] = int(input("Rolle:"))

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
playerObj.items = input("Gegenstände:")
playerObj.numbers = input("Anzahlen:")
playerObj.inventory = dict(zip(playerObj.items, playerObj.numbers))

print(playerObj.look)
print(playerObj.attributes)
print(playerObj.inventory)

