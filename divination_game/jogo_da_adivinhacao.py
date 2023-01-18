from random import randrange


def number_computer():
    computer_number = randrange(0, 11)
    return computer_number


def number_player():
    player_number = int(input('Digite um número: '))
    return player_number


def start():
    computer = number_computer()
    
    count = 10

    while count:
        player = number_player()

        if player < computer:
            print('Tente um número mais maior.')
            count -= 1
            print(f'Você tem {count} tentativas')

        elif player > computer:
            print('Tente um número menor')
            count -= 1
            print(f'Você tem {count} tentativas')
        
        elif player == computer:
            print(f'Parabéns, você acertou. É o {computer}!')

    print(f'Você perdeu. O número era {computer}.')


start()