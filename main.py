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
curaga = Spell(name="Curaga", cost=50, dmg=2000, type="white")

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, curaga]

# Create some Items
potion = Item(name="Potion", type="potion", description="Heals 50 HP", prop=50)
hiPotion = Item(name="High Potion", type="potion", description="Heals 100 HP", prop=100)
superPotion = Item(name="Super Potion", type="potion", description="Heals 100 HP", prop=1000)
elixer = Item(name="Elixer", type="elixer", description="Fully restores HP/MP of one party member", prop=9999)
hiElixer = Item(name="Mega Elixer", type="elixer", description="Fully restores party's HP/MP", prop=9999)
grenade = Item(name="Grenade", type="attack", description="Deals 500 damage", prop=500)

player_items = [{"item": potion, "quantity": 5}, {"item": hiPotion, "quantity": 5},
                {"item": superPotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hiElixer, "quantity": 5}, {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person(name="Varon ", hp=3300, mp=450, atk=350, df=34, magic=player_spells, items=player_items)
player2 = Person(name="Erina ", hp=2500, mp=250, atk=200, df=34, magic=player_spells, items=player_items)
player3 = Person(name="Karin ", hp=5000, mp=650, atk=400, df=34, magic=player_spells, items=player_items)
players = [player1, player2, player3]
enemy1 = Person(name="Nulle ", hp=3000, mp=1000, atk=600, df=335, magic=enemy_spells, items=[])
enemy2 = Person(name="Baron ", hp=12000, mp=1500, atk=525, df=25, magic=enemy_spells, items=[])
enemy3 = Person(name="Stan  ", hp=2400, mp=1000, atk=750, df=150, magic=enemy_spells, items=[])
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(""""\n\n  _____  _____   _____            ____       _______ _______ _      ______ 
 |  __ \|  __ \ / ____|          |  _ \   /\|__   __|__   __| |    |  ____|
 | |__) | |__) | |  __   ______  | |_) | /  \  | |     | |  | |    | |__   
 |  _  /|  ___/| | |_ | |______| |  _ < / /\ \ | |     | |  | |    |  __|  
 | | \ \| |    | |__| |          | |_) / ____ \| |     | |  | |____| |____ 
 |_|  \_\_|     \_____|          |____/_/    \_\_|     |_|  |______|______|
""")

print(Colors.fail + Colors.bold + """\n\t\t\t\t\t  MUSUH DATANG MENYERANG!
\t\t   AYO KALAHKAN MUSUH-MUSUH YANG ADA DI DEPANMU!""" + Colors.endc)
while running:
    print("\n_______________________________________________________________________")
    print(Colors.okGreen + Colors.bold + "\t\t\t\t\t\t\tSTATUS PEMAIN" + Colors.endc)
    print("───────────────────────────────────────────────────────────────────────")
    print("NAMA                 DARAH                                  MANA")
    print("_______________________________________________________________________")
    for player in players:
        player.get_stats()
    print("───────────────────────────────────────────────────────────────────────")

    print("\n")
    print("_______________________________________________________________________")
    print(Colors.fail + Colors.bold + "\t\t\t\t\t\t\tSTATUS MUSUH" + Colors.endc)
    print("───────────────────────────────────────────────────────────────────────")
    print("NAMA                 DARAH                                     ")
    print("_______________________________________________________________________")
    for enemy in enemies:
        enemy.get_enemy_stats()
    print("───────────────────────────────────────────────────────────────────────")

    for player in players:
        player.choose_action()
        choice = int(input("Choose action : "))
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)

            print("\nYou attacked ", enemies[enemy].name.replace(" ", ""), "for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]

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
                      enemies[enemy].name.replace(" ", "") + Colors.endc)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

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
                      enemies[enemy].name.replace(" ", "") + Colors.endc)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

    # Checked if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Checked if player won
    if defeated_enemies == 2:
        print(Colors.okGreen + "You win!" + Colors.endc)
        running = False

    # Checked if enemy won
    elif defeated_players == 2:
        print(Colors.fail + "Your enemies has defeated you!" + Colors.endc)
        running = False

    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Choose attack
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print("\n" + Colors.fail + enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "")
                  + " for", enemy_dmg, "points of damage." + Colors.endc)

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)

                print(Colors.okGreen + "\n" + spell.name + " heals " + enemy.name + "for", str(magic_dmg), "HP." +
                      Colors.endc)

            elif spell.type == "black":
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg)

                print(Colors.okBlue + "\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg),
                      "points of damage to", players[target].name.replace(" ", "") + Colors.endc)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[target]
