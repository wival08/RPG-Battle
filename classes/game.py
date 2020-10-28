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
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkL = atk - 10
        self.atkH = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkL, self.atkH)