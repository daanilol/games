from random import randrange


def welcome_message():
    print(64 * "*")
    print('''Opa! Bem vindo ao jogo da Forca.
Você terá em chances a quantidade de letras da palavra sorteada.
Leia as informações atualizadas a cada rodada para jogar!''')
    print(64 * "*")


def secret_word_generator():
    arquive = open('word_list.txt', 'r', encoding='utf-8')
    correct_letter = []

    for word in arquive:
        word = word.strip()
        correct_letter.append(word)

    arquive.close()

    number_of_word = randrange(0, len(correct_letter))
    secret_word = correct_letter[number_of_word].upper()
    return secret_word


def win_message():

    print('''\n             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`''')


def lose_message(secret_word):

    print(f'''\n   A palavra correta é: {secret_word}
                                 |/|
                                 |/|
                                 |/|
                                 |/|
                                 |/|
                                 |/|
                                 |/| /�)
                                 |/|/\/
                                 |/|\/
                                (���)
                                (���)
                                (���)
                                (���)
                                (���)
                                /��/
                               / ,^./)
                              / /   \/)
                             / /     \/)
                            ( (       )/)
                            | |       |/|
                            | |       |/|
                            | |       |/|
                            ( (       )/)
                             \ \     / /
                              \ `---' /
                               `-----'   ''')


def play_game():
    welcome_message()
    secret_word = secret_word_generator()
    correct_letter = ["_" for letter in secret_word]

    hanged = False
    win = False
    error = len(secret_word)

    print(f"\n{correct_letter}")

    while (not hanged and not win):
        attempt = input('\nDigite uma letra: ')
        attempt = attempt.strip().upper()

        if attempt in secret_word:
            index = 0
            for letter in secret_word:
                if letter == attempt:
                    correct_letter[index] = letter
                index += 1

        else:
            error -= 1
            print(f"Restam apenas {error} tentativas.")


        hanged = error == 0
        win = "_" not in correct_letter

        print(correct_letter)

    if hanged:
        lose_message(secret_word)
        

    if win:
        win_message()

play_game()