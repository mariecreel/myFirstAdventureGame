"""
my first text based adventure game.

getting used to the kind of programming you have to do for adventure games
hopefully giving me some insight on what the design process is like
for a programmer and where the hurdles might be for novice programmers.

- nick c.

this file contains all class definitions.
"""
import re
from random import randint

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

    def __init__(self, defense = 10):
        self.inventory = {}
        self.location = None
        self.hp = 10
        self.maxHP = 10
        self.isDead = False
        self.attributes = {"STR":0,
                           "CON":0,
                           "DEX":0,
                           "INT":0,
                           "WIN":0,
                           "CHA":0}
        self.defense = defense

    def attack(self, target):
        attackRoll = randint(1, 21)
        if self.weapon == None:
            if attackRoll + self.attributes["STR"] > target.defense:
                target.hp = target.hp - self.attributes["STR"]
                if target.hp > 0:
                    print(f"{self.name}'s attack hits!")
                    print(f"{target.name} takes {self.attributes["STR"]} damage.")
                else:
                    target.isDead = True
                    print(f"{self.name}'s attack hits!")
                    print(f"{target.name} collapses.")
            else:
                print(f"{self.name}'s attack misses!")
        elif self.weapon != None:
            if attackRoll + self.attributes["DEX"] > target.defense:
                target.hp = target.hp - self.weapon.damage
                if target.hp > 0:
                    print("{self.name} lands a blow with {self.weapon.name}!")
                    print("{target.name} takes {self.weapon.damage} damage!")
                else:
                    target.isDead = True
                    print("{self.name} lands a blow with {self.weapon.name}!")
                    print(f"{target.name} collapses.")
            else:
                print(f"{self.name}'s attack misses!")

    def attributesRoll(self):
        """
        Actor.attributesRoll: rolls a 6 sided die four times, takes the 3 most
        maximum values of those and returns the sum of those 3 values.
        meant to emulate attribute rolls in DND character creation.
        """
        rolls = []
        total = 0
        for key in self.attributes:
            for i in range(0, 4):
                rolls.append(randint(1,6))
            for i in range(0,3):
                total += rolls.pop(max(rolls))
            self.attributes[key] = total
            rolls = []

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
