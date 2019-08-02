"""
my first text based adventure game.

getting used to the kind of programming you have to do for adventure games
hopefully giving me some insight on what the design process is like
for a programmer and where the hurdles might be for novice programmers.

- nick c.

this file contains all class definitions.
"""
class GameObject:
    """GameObject: all other classes are descendants of this"""
    def __init__(self, name, type, description):
        self.name = name
        self.description = description

class Actor(GameObject):

    def __init__(self):
        self.inventory = {}
        self.location = None

    def useItem(self, item_name):
        if item_name in self.inventory:
            self.inventory[item_name].use()
        else:
            print(f"There doesn't seem to be a(n) {item_name} in your inventory")

    def dropItem(self, item_name):
        try:
            del self.inventory[item_name]
        except KeyError as ex:
            print(f"There doesn't seem to be a(n) {item_name} in your inventory")
            
class Item(GameObject):
    def __init__(self, isResuable = 0, isWeapon = False, self.isContainer = False):
        self.isReusable = isReusable #0 == no, else num value is number of times
                                     #player can use item
        self.isWeapon = isWeapon
        self.attributes = []
        self.isContainer = isContainer

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
