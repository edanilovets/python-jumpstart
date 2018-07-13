from actors import Wizard, Creature


creatures = [
    Creature('Toad', 1),
    Creature('Bat', 3),
    Creature('Tiger', 12),
    Creature('Dragon', 50),
    Creature('Evil Wizard', 1000)
]


hero = Wizard('Gandalf', 75)


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------')
    print('       WIZARDS GAME')
    print('--------------------------')
    print()


def game_loop():

    while True:
        cmd = input('Do you [a]ttack, [r]un away, [l]ook around? ')
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')
        else:
            print('Exiting game!...')
            break


if __name__ == '__main__':
    main()
