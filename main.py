from classes.game import Person, Colors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 12, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(Colors.fail + Colors.bold + "\n\t\t\t\t\tAN ENEMY ATTACKS!" + Colors.endc)

while running:
    print("==========================================================")
    player.choose_action()
    choice = int(input("Choose action : "))
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic : ")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(Colors.fail + "\nNot enough MP\n" + Colors.endc)
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(Colors.okBlue + "\n" + spell + " deals", str(magic_dmg), "points of damage" + Colors.endc)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")

    print("-----------------------------")
    print("Enemy HP : ", Colors.fail + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Colors.endc + "\n")

    print("Your HP : ", Colors.okGreen + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Colors.endc)
    print("Yout MP : ", Colors.okBlue + str(player.get_mp()) + "/" + str(player.get_max_mp()) + Colors.endc + "\n")

    if enemy.get_hp() == 0:
        print(Colors.okGreen + "You win!" + Colors.endc)
        running = False
    elif player.get_hp() == 0:
        print(Colors.fail + "Your enemy has defeated you!" + Colors.endc)
        running = False





