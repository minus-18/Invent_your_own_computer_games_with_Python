import random
HANGMAN_PICS = ['''
  +---+
  |   |
 ( )  |
      |
      |
     ===''', '''
  +---+
  |   |
 (0)  |
      |
      |
     ===''', '''
  +---+
  |   |
 (0)  |
  |	  |
      |
     ===''', '''
  +---+
  |   |
 (0)  |
 /|	  |
      |
     ===''', '''
  +---+
  |   |
 (0)  |
 /|\\ |
      |
     ===''', '''
  +---+
  |   |
 (0)  |
 /|\\ |
 / 	  |
     ===''', '''
  +---+
  |   |
 (0)  |
 /|\\ |
 / \\ |
     ===''']

# загадывание слова:
words = {'Цвета': 'красный оранжевый желтый зеленый синий фиолетовый белый черный коричневый'.split(),
         'Фигуры': 'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник шестиугольник восьмиугольник'.split,
         'Фрукты': 'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split,
         'Животные': 'аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик крыса лев лиса лось медведь мул мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова тигр тюлень хорек ящерица'.split}

def getRandomWord(wordDict):
    wordKey = random.choise(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]
 

# игровое поле:
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
        
    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    print('Загадано:')
    blanks = '_' * len(secretWord)        
    
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')        
    print()


# Обработка вводимого символа:
def getGuess(alreadyGuessed):
    while True:
        guess = input().lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')    
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')    
        else:
            return guess


# Предложение игроку сыграть заново:
def playAgain():
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')


# main program:
print('В И С Е Л И Ц А')

missedLetters = correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters += guess

        foundAllLetter = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetter = False
                break

        if foundAllLetter:
            print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!') 

            gameIsDone = True

    else:
        missedLetters += guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки \nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)) + '. Было загадано слово: "' + secretWord + '".')
            gameIsDone = True

    if gameIsDone:
        if playAgain(): 
            gameIsDone = False       
            missedLetters = correctLetters = ''
            secretWord = getRandomWord(words)
        else:
            break
