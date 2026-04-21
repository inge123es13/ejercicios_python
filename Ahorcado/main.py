# Programa para jugar el ahorcado

import random

def get_word(file_name):
    words = []
    with open(file_name, 'r') as file:
        for line in file:
            words.append(line.strip())  # quitar saltos de línea
    length = len(words)
    index = random.randint(0, length - 1)
    return words[index]

def draw_hangman(errors):

    match(errors):
        case 1:
            hangman = '''
        |- - - - - - - 
        |
        |
        |
        |
        |
        |
        |
        |______________________________
        '''
        case 2:
            hangman = '''
        |- - - - - - - 
        |        |
        |
        |
        |
        |
        |
        |
        |______________________________
        '''
        case 3:
            hangman = '''
        |- - - - - - -  - 
        |        |
        |        O
        |
        |
        |
        |
        |
        |______________________________
        '''
        case 4:
            hangman = '''
        |- - - - - - - 
        |        |
        |        O
        |        |
        |        |
        |
        |
        |
        |______________________________
        '''
        case 5:
            hangman = '''
        |- - - - - - - - - -
        |        |
        |        O
        |       /|\\
        |        |
        |
        |
        |
        |______________________________
        '''
        case 6:
            hangman = '''
        |- - - - - - - - - -
        |        |
        |        O
        |       /|\\
        |        |
        |       / \\
        |
        |
        |______________________________
        '''
        case _:
            hangman = ""

    print(hangman)

# función que regresa guiones en lugar de la palabra 
def get_dashed_word(word, chars=''):
    dashed_word = '-' * len(word)
    for char in chars:
        new_word = ''
        for i in range(len(word)):
            if word[i] == char:
                new_word += char
            else:
                new_word += dashed_word[i]
        dashed_word = new_word
    return dashed_word

def select_category():
    choices_menu = "Elige la categoria para jugar"
    choices_menu += "\n1. Comidas\n2. Animales\n3. Equipos:\n"
    
    try:
        choice = int(input(choices_menu))
    except:
        print("Entrada inválida")
        return None

    if choice == 1:
        word = get_word('Comidas.txt')
    elif choice == 2:
        word = get_word('Animales.txt')
    elif choice == 3:
        word = get_word('Equipos.txt')
    else:
        print('Opción Incorrecta')
        return None

    return word

def game():
    print('Bienvenido al juego del Ahorcado')
    word = select_category()

    if word != None:
        print(get_dashed_word(word))

        chars = ''
        errors = 0

        while True:
            char = input('Ingresa una letra o la palabra completa: ')

            if len(char) == 1:
                if char in word:
                    chars += char
                else:
                    errors += 1
                    draw_hangman(errors)
            else:
                if char == word:
                    print("¡Ganaste!")
                    break
                else:
                    errors += 1
                    draw_hangman(errors)

            print(get_dashed_word(word, chars))

            if get_dashed_word(word, chars) == word:
                print("¡Ganaste!")
                break

            if errors == 6:
                print("Perdiste. La palabra era:", word)
                break
    else:
        return

if __name__ == "__main__":
    game()