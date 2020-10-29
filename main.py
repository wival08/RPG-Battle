from classes.game import Person, Colors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Instantie People
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

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





