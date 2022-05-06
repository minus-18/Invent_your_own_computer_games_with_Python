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
 /|\\  |
      |
     ===''', '''
  +---+
  |   |
 (0)  |
 /|\\  |
 / 	  |
     ===''', '''
  +---+
  |   |
 (0)  |
 /|\\  |
 / \\  |
     ===''']

# загадывание слова:
words = {'цвета': 'красный оранжевый желтый зеленый синий фиолетовый белый черный коричневый'.split(),
         'фигуры': 'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник шестиугольник восьмиугольник'.split(),
         'фрукты': 'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split(),
         'животные': 'аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик крыса лев лиса лось медведь мул мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова тигр тюлень хорек ящерица'.split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]
 

# игровое поле:
def displayBoard(missedLetters, correctLetters, secretWord, secretSet):
    print(HANGMAN_PICS[len(missedLetters)])

    print('Загадано слово из набора - ', secretSet, ':', sep='')
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()
    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()



# Обработка вводимого символа:
def getGuess(alreadyGuessed):
    while True:
        guess = input('Введите букву загаданного слова: ').lower()
        if len(guess) != 1:
            print('Пожалуйста, введите ОДНУ букву.')
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

difficulty = ''
while difficulty not in 'EMH':
    difficulty = input('Выбирите уровень сложности: E - легкий, M - средний, H - тяжелый: ').upper()
if difficulty == 'M':
    del HANGMAN_PICS[0]
    del HANGMAN_PICS[1]
if difficulty == 'H':
    del HANGMAN_PICS[0]
    del HANGMAN_PICS[1]
    del HANGMAN_PICS[2]
    del HANGMAN_PICS[3]

missedLetters = correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord, secretSet)

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
            displayBoard(missedLetters, correctLetters, secretWord, secretSet)
            print('Вы исчерпали все попытки \nНеверных попыток: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)) + '. Было загадано слово: "' + secretWord + '".')
            gameIsDone = True

    if gameIsDone:
        if playAgain(): 
            gameIsDone = False       
            missedLetters = correctLetters = ''
            secretWord = getRandomWord(words)
        else:
            break
