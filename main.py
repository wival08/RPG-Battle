import random
from classes.game import Person, Colors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell(name="Fire", cost=25, dmg=550, type="black")
thunder = Spell(name="Thunder", cost=30, dmg=750, type="black")
blizzard = Spell(name="Blizzard", cost=35, dmg=640, type="black")
meteor = Spell(name="Meteor", cost=60, dmg=1600, type="black")
quake = Spell(name="Quake", cost=45, dmg=870, type="black")

# Create White Magic
cure = Spell(name="Cure", cost=35, dmg=620, type="white")
cura = Spell(name="Cura", cost=60, dmg=1600, type="white")

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]

# Create some Items
potion = Item(name="Potion", type="potion", description="Heals 50 HP", prop=50)
hiPotion = Item(name="High Potion", type="potion", description="Heals 100 HP", prop=100)
superPotion = Item(name="Super Potion", type="potion", description="Heals 100 HP", prop=1000)
elixer = Item(name="Elixer", type="elixer", description="Fully restores HP/MP of one party member", prop=9999)
hiElixer = Item(name="Mega Elixer", type="elixer", description="Fully restores party's HP/MP", prop=9999)
grenade = Item(name="Grenade", type="attack", description="Deals 500 damage", prop=500)

player_items = [{"item": potion, "quantity": 5}, {"item": hiPotion, "quantity": 5},
                {"item": superPotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hiElixer, "quantity": 5}, {"item":grenade, "quantity": 5}]

# Instantiate People
player1 = Person(name="Varon:", hp=3300, mp=450, atk=350, df=34, magic=player_spells, items=player_items)
player2 = Person(name="Erina:", hp=2500, mp=250, atk=200, df=34, magic=player_spells, items=player_items)
player3 = Person(name="Karin:", hp=5000, mp=650, atk=400, df=34, magic=player_spells, items=player_items)
players = [player1, player2, player3]
enemy1 = Person(name="Nulle ", hp=3000, mp=100, atk=600, df=335, magic=[], items=[])
enemy2 = Person(name="Baron ", hp=12000, mp=500, atk=525, df=25, magic=[], items=[])
enemy3 = Person(name="Stan  ", hp=2400, mp=80, atk=750, df=150, magic=[], items=[])
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(Colors.fail + Colors.bold + "\n\n\t\t\tAN ENEMY ATTACKS!" + Colors.endc)

while running:
    print("=======================================")

    print("\n\n")
    print("NAME                 HP                                   MP")
    for player in players:
        player.get_stats()
    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = int(input("Choose action : "))
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("\nYou attacked ", enemies[enemy].name, "for", dmg, "points of damage.")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic : ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(Colors.fail + "\nNot enough MP\n" + Colors.endc)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(Colors.okBlue + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + Colors.endc)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(Colors.okBlue + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to ",
                      enemies[enemy].name + Colors.endc)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item : ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(Colors.fail + "\n" + "None Left..." + Colors.endc)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(Colors.okGreen + "\n" + item.name + " heals for", str(item.prop), "HP" + Colors.endc)
            elif item.type == "elixer":
                if item.name == "Mega Elixer":
                    for i in players:
                        i.hp = player.maxHp
                        i.mp = player.maxMp
                else:
                    player.hp = player.maxHp
                    player.mp = player.maxMp
                print(Colors.okGreen + "\n" + item.name + " fully restores HP/MP" + Colors.endc)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(Colors.fail + "\n" + item.name + " deals", str(item.prop), "points of damage to",
                      enemies[enemy].name + Colors.endc)

    enemy_choice = 1
    target = random.randrange(0, 3)
    enemy_dmg = enemies[0].generate_damage()

    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")

    if enemies.get_hp() == 0:
        print(Colors.okGreen + "You win!" + Colors.endc)
        running = False
    elif player.get_hp() == 0:
        print(Colors.fail + "Your enemy has defeated you!" + Colors.endc)
        running = False






