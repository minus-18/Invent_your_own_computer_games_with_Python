# Это игра по угадыванию чисел.
import random

guessTaken = 0

print('Привет, как тебя зовут?')
myName = input('Напиши своё имя: ')

total, limit = 6, 100

number = random.randint(1,limit)

print(f'Что ж, {myName}, я загадываю число от 1 до {limit}.')

for _ in range(total):

	guessTaken += 1

	print(f'Попробуй угадать. Твоя {guessTaken}-я попытка. Останется {total - guessTaken}') 

	guess = int(input())

	if guess < number:
		print('Твоё число меньше загаданного')		
	elif guess > number:
		print('Твоё число больше загаданного')	
	else:
		print(f'Отлично, {myName}! Ты справился с {guessTaken}-го раза')	
		break
else:
	print(f'Увы. Ты не угадал число {number} за {total} попыток.')
	

		
