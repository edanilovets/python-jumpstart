
#
# WIZARD BATTLE
#

import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon


creatures = [
    SmallAnimal('Toad', 1),
    SmallAnimal('Bat', 3),
    Creature('Tiger', 12),
    Dragon('Drogon', 30, 75, True),
    Dragon('Viserion', 50, 25, False),
    Dragon('Rhaegal', 30, 45, True),
    Wizard('Evil Wizard', 1000)
]


hero = Wizard('Gandalf', 75)


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------')
    print('       WIZARD BATTLE')
    print('--------------------------')
    print()


def game_loop():

    while True:
        active_creature = random.choice(creatures)
        print('\nA {} of level {} appeared from dark forest...\n'.format(
            active_creature.name, active_creature.level
        ))

        cmd = input('Do you [a]ttack, [r]un away, [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides taking time to recover...%-)')
                time.sleep(5)
                print('The wizard returns full of power!')
        elif cmd == 'r':
            print('The wizard is a coward and runs away! Ha-ha-ha...')
        elif cmd == 'l':
            print('The wizard {} looks around and sees: '.format(hero.name))
            for c in creatures:
                print('* {} of level {}'.format(c.name, c.level))
        else:
            print('Exiting game...')
            break

        if not creatures:
            print('\nYou left alone, game over! Ha-ha-ha\nexiting game...\n')
            break


if __name__ == '__main__':
    main()
