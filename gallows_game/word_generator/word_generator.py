from random import randrange


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


if __name__ == '__main__':
    secret_word_generator()