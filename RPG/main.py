from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


# Create black magic
fire = Spell("Fire", 5, 70, "black")
thunder = Spell("Thinder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 13, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Items

potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
hielixer = Item("Mega-Elixer", "elixer", "Fully restore HP/MP", 9999)

grenate = Item("Grenage", "attack", "Deals 500 damage", 500)

player_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemies_magic = [fire, thunder, meteor, cure]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2},
                {"item": grenate, "quantity": 5}]

# Instantiate People
player1 = Person("Silvana:  ", 460, 65, 150, 34, player_magic, player_items)
player2 = Person("Trall:    ", 460, 65, 150, 34, player_magic, player_items)
player3 = Person("Ragnaros: ", 460, 65, 150, 34, player_magic, player_items)

enemy1 = Person('Imp         ', 130, 100, 222, 325, enemies_magic, [])
enemy2 = Person("Lich King:", 1200, 100, 110, 25, enemies_magic, [])
enemy3 = Person('Imp         ', 130, 100, 222, 325, enemies_magic, [])

players = [player1, player2, player3]

enemies = [enemy1, enemy2, enemy3]


running = True

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!' + bcolors.ENDC)

def show_details():
    print("=======================")
    print("\n\n")
    print('NAME                       HP                                   MP')
    for player in players:
        player.get_stats()
    print('\n')
    for enemy in enemies:
        enemy.get_enemy_stats()


while running:
    show_details()

    for player in players:
        if len(enemies) < 1:
            print(bcolors.OKGREEN + 'You win!' + bcolors.ENDC)
            running = False
            show_details()
            break
        player.choose_action()
        choice = input('Choose action:')
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print('You attacked', enemies[enemy].name.replace(" ", ""), ' for', dmg, 'points of damage.')

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + ' has died')
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input('Choose Magic: ')) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + '\n Not enought mp\n' + bcolors.ENDC)
                continue


            player.reduce_mb(spell.cost)

            if spell.type == 'white':
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + '\n' + spell.name + ' heals for', str(magic_dmg), 'HP.' + bcolors.ENDC)
            elif spell.type == 'black':
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + '\n' + spell.name + ' deals', str(magic_dmg), 'points of damage to ' + enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choise = int(input("Choose item: ")) - 1

            if item_choise == -1:
                continue

            item = player.items[item_choise]["item"]
            if player.items[item_choise]["quantity"] == 0:
                print(bcolors.FAIL + '\n' + 'None left...' + bcolors.ENDC)
                continue
            player.items[item_choise]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + '\n' + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == 'elixer':
                if item.name == 'MegaElexir':
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + '\n' + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == 'attack':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + '\n' + item.name + ' deals', str(item.prop), "points of damage to " + enemies[enemy].name + bcolors.ENDC)

    # Check if batle over

    defeated_enemies = 0
    defeated_players = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if Player won

    if defeated_enemies == 2:
        print(bcolors.OKGREEN + 'You win!' + bcolors.ENDC)
        running = False

    # Check if Enemies won

    elif defeated_players == 2:
        print(bcolors.FAIL + 'Your enemies have defeated you' + bcolors.ENDC)
        running = False

    #Enemy attack phase

    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            # Chose attack
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + "Enemy attacks " + players[target].name.replace(" ", '') + " for " + str(enemy_dmg))
        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()

            enemy.reduce_mb(spell.cost)
            print("Enemy chose ", spell.name, ' damage is ', magic_dmg)


            if spell.type == 'white':
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + '\n' + spell.name + ' heals ' + enemy.name.replace(" ", '') +' for', magic_dmg, 'HP.' + bcolors.ENDC)
            elif spell.type == 'black':
                target = random.randrange(0, 3)

                players[target].take_damage(int(magic_dmg))

                print(bcolors.OKBLUE + '\n' + enemy.name.replace(' ', '') + "'s " + spell.name + ' deals', magic_dmg,
                      'points of damage to ' + players[target].name + bcolors.ENDC)
                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died")
                    del players[target]
