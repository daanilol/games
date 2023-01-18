from random import randint
import time 


def divination_welcome_message():
    print('\n')
    print(19 * '*')
    print('Jogo da Adivinhação')
    print(19 * '*')


def status(chance, points, error):
    print(f'O número que você terá que descobrir está entre 1 e {chance}.')
    print(f'\nVocê tem {chance} tentativas')
    print(f'Você começará com {points} pontos.')
    print(f'Se errar, perderá {error} pontos.')
    print('Tente terminar o jogo com o maior número de pontos possível.\n')
    print('\n\nNíveis de dificuldade: (1) Easy (2) Normal (3) Hard')


def divination_start_game():
    divination_welcome_message()

    level = 0
    chance = 0 
    points = 0
    error = 0
    divination_welcome_message()

    while level not in [1, 2, 3]:
        level = int(input('Selecione o nível do jogo: '))
        if level == 1:
            chance = 20 
            points = 150
            error = 7.5
        
        elif level == 2:
            chance = 10
            points = 75
            error = 7.5

        elif level == 3:
            chance = 5
            points = 37.5
            error = 7.5

        else:
            print('Favor selecionar uma opção válida.')
                
    status(chance, points, error)

    print('[Máquina pensando]')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('...\n')

    computer = randint(1, chance)

    for c in range(1, chance + 1):
        print(f'Tentativa {c} de {chance}')
        player = int(input('\nAgora, tente adivinhar.\nDigite um número: '))
        
        if player == computer:
            print('Parabéns, você ganhou!')
            print(f'Finalizou com {points}, pontos.')
            break

        elif player < 1 or player > chance:
            print(f'Favor escolher um número entre 1 e {chance}')
            points -= error
            print(f'Pontos: {points}\n')
        
        else:
            if player > computer:
                if c < chance:
                    print(f'Seu número é maior que o número pensado pelo computador.')
                    points -= error
                    print(f'Pontos: {points}\n')

            elif player < computer:
                if c < chance:
                    print(f'Seu número é menor que o número pensado pelo computador.\n')
                    points -= error
                    print(f'Pontos: {points}\n')

        if c == chance:
            print('Você perdeu.')

if __name__ == '__main__':
    divination_start_game()


