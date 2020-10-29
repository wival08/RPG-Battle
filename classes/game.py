import random


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

    def choose_target(self, enemies):
        i = 1
        print("\n" + Colors.fail + Colors.bold + "TARGET" + Colors.endc)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("\t" + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("\t" + "Choose target : ")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxHp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxHp)
        current_hp = ""

        if len(hp_string) < 11:
            hp_decrease = 11 - len(hp_string)

            while hp_decrease > 0:
                current_hp += " "
                hp_decrease -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                      __________________________________________________ ")
        print(Colors.bold + self.name + "   " +
              current_hp + " |" + Colors.fail + hp_bar + Colors.endc + "|")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxHp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxMp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxHp)
        current_hp = ""

        if len(hp_string) < 9:
            hp_decrease = 9 - len(hp_string)

            while hp_decrease > 0:
                current_hp += " "
                hp_decrease -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxMp)
        current_mp = ""

        if len(mp_string) < 7:
            mp_decrease = 7 - len(mp_string)

            while mp_decrease > 0:
                current_mp += " "
                mp_decrease -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                     _________________________              __________ ")
        print(Colors.bold + self.name + "    " +
              current_hp + " |" + Colors.okGreen + hp_bar + Colors.endc + "|" + Colors.bold + "    " +
              current_mp + " |" + Colors.okBlue + mp_bar + Colors.endc + "|")

