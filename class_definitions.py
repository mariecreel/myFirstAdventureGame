"""
my first text based adventure game.

getting used to the kind of programming you have to do for adventure games
hopefully giving me some insight on what the design process is like
for a programmer and where the hurdles might be for novice programmers.

- nick c.

this file contains all class definitions.
"""
import re

class GameObject:
    """GameObject: all other classes are descendants of this"""
    def __init__(self, name, type, description):
        self.name = name
        self.description = description

class Actor(GameObject):
    """
    Actor: all characters, npc or pc, are actors. Actors can use items,
    drop items, grab items, talk, navigate the game world, and battle.
    Actors possess a number of attributes which determines how likely
    it is that they will be successful when taking certain actions.
    """
    direction_key = {"n":"north",
                     "s":"south",
                     "e":"east",
                     "w":"west"}
    vowels = "aeiouAEIOU"
    def __init__(self, species="Cat", class="House Cat", size = "Small", isPC = False):
        self.inventory = {}
        self.location = None
        self.attributes = {"Species":species,
                           "Class":class,
                           "Size":size}
        self.isPC = isPC
    def attributesRoll(self):
        

    def useItem(self, item_name):
        if item_name in self.inventory:
            self.inventory[item_name].use()
        else:
            vowel = re.search(vowels, item_name[0])
            if vowel:
                print(f"There doesn't seem to be an {item_name} in your inventory")
            else:
                print(f"There doesn't seem to be a {item_name} in your inventory")

    def dropItem(self, item_name):
        try:
            del self.inventory[item_name]
        except KeyError as ex:
            vowel = re.search(vowels, item_name[0])
            if vowel:
                print(f"There doesn't seem to be an {item_name} in your inventory")
            else:
                print(f"There doesn't seem to be a {item_name} in your inventory")

    def move(self, direction):
        if direction = "w" and self.location.w != None:
            self.location = self.location.w
        elif direction = "n" and self.location.n != None:
            self.location = self.location.n
        elif direction = "s" and self.location.s != None:
            self.location = self.location.s
        elif direction = "e" and self.location.e != None:
            self.location = self.location.e
        else:
            print(f"You cannot travel to the {direction_key[direction]} from here.")

class Item(GameObject):
    def __init__(self, isResuable = 0, isWeapon = False, self.isContainer = False):
        self.isReusable = isReusable #0 == no, else num value is number of times
                                     #player can use item
        self.isWeapon = isWeapon
        self.attributes = {}
        self.isContainer = isContainer
        self.contents = {}

class Scene(GameObject):
    def __init__(self, n=None, s=None, e=None, w=None):
        self.north = n
        self.south = s
        self.east = e
        self.west = w
        self.contents = {}

    def addItem(self, item):
        self.contents[item.name] = item

    def addItems(self, items):
        for item in items:
            self.contents[item.name] = item
