from random import randrange


def word_generator():
  arq = open('word_list.txt', 'r', encoding='utf-8')
  word_list = []

  for line in arq:
    line = line.strip()
    word_list.append(line)

  arq.close()

  number = randrange(0, len(word_list))
  secret_word = word_list[number].upper()
  return secret_word


def start():
  secret_word = word_generator()
  letters_in_word = ["_" for letter in secret_word]

  hanged = False
  win = False
  error = len(secret_word)
  
  while (not hanged and not win):
    
    attempt = input('Digite uma letra: ')
    attempt = attempt.strip().upper()

    if attempt in secret_word:
      index = 0
      for letter in secret_word:
        if letter == attempt:
          letters_in_word[index] = letter
        index += 1
    
    elif attempt not in secret_word:
      print(f'Você errou. Tente novamente, tem apenas [{error}] chances.')
      error -= 1

    hanged = error == 0
    win = "_" not in letters_in_word

    print(letters_in_word)

  if hanged:
    print(f'Você perdeu. A palavra correta era {secret_word}.')

  elif win:
    print(f'Parabéns, a palavra correta é {secret_word}.')


start()