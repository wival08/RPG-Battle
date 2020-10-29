import random
from .magic import Spell


class Colors:
    header = '\033[95m'
    okBlue = '\033[94m'
    okGreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[15m'
    underline = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkL = atk - 10
        self.atkH = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkL, self.atkH)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + Colors.bold + self.name + Colors.endc)
        print(Colors.okBlue + Colors.bold + "ACTIONS" + Colors.endc)
        for action in self.actions:
            print("\t" + str(i) + ":", action)
            i += 1

    def choose_magic(self):
        i = 1
        print(Colors.okBlue + Colors.bold + "\nMAGIC" + Colors.endc)
        for spell in self.magic:
            print("\t" + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1

        print(Colors.okBlue + Colors.bold + "\nITEMS" + Colors.endc)
        for item in self.items:
            print("\t" + str(i) + ".", item["item"].name + ":",
                  item["item"].description,
                  "(x" + str(item["quantity"]) + ")")
            i += 1

    def get_stats(self):
        print("                     _________________________            __________ ")
        print(Colors.bold + self.name + "    " + str(self.hp) + "/" + str(self.maxHp) + " |" +
              Colors.fail + "█████████████████████████" +
              Colors.endc + "|" + Colors.bold + "    " + str(self.mp) + "/" + str(self.maxMp) + " |" +
              Colors.okBlue + "██████████" + Colors.endc + "|")

