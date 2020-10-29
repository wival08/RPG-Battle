from classes.game import Person, Colors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hiPotion = Item("High Potion", "potion", "Heals 100 HP", 100)
superPotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hiElixer = Item("Mega Elixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 5}, {"item": hiPotion, "quantity": 5},
                {"item": superPotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hiElixer, "quantity": 5}, {"item":grenade, "quantity": 5}]

# Instantiate People
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(Colors.fail + Colors.bold + "\n\t\t\tAN ENEMY ATTACKS!" + Colors.endc)

while running:
    print("=======================================")
    player.choose_action()
    choice = int(input("Choose action : "))
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("\nYou attacked for", dmg, "points of damage.")
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
            enemy.take_damage(magic_dmg)
            print(Colors.okBlue + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + Colors.endc)

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
            player.hp = player.maxHp
            player.mp = player.maxMp
            print(Colors.okGreen + "\n" + item.name + " fully restores HP/MP" + Colors.endc)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(Colors.fail + "\n" + item.name + " deals", str(item.prop), "points of damage" + Colors.endc)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")

    print("---------------------------------------")
    print("\nEnemy HP : ", Colors.fail + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Colors.endc + "\n")

    print("Your HP : ", Colors.okGreen + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Colors.endc)
    print("Your MP : ", Colors.okBlue + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Colors.endc + "\n")

    if enemy.get_hp() == 0:
        print(Colors.okGreen + "You win!" + Colors.endc)
        running = False
    elif player.get_hp() == 0:
        print(Colors.fail + "Your enemy has defeated you!" + Colors.endc)
        running = False






