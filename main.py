from Charactersystem import Newcharacter

def print_list(attr_list):
  for i, val in enumerate(attr_list):
    print(str(i) + ":", val)

playerObj = Newcharacter()

playerObj.name = input("Name:")
print(playerObj.name)

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

print(playerObj.look)