import random
import time

def displayIntro():
	print('''Вы находитесь в землях, заселенных драконами.
		Перед собой вы видите две пещеры. В одной из них - дружелюбный дракон, 
		который готов поделиться с вами своими сокровищами. Во второй -
		жадный и голодный дракон,который мигом вас съест. ''')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('В какую пещеру вы войдете? (1 или 2)')
		cave = input()
	print()	
	return cave	

def checkCave(chooseCave):
	print('Вы приближаетесь к пещере...')
	time.sleep(2)	
	print('Её темнота заставляет вас дрожать от страха...')
	time.sleep(2)
	print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
	print()
	time.sleep(2)

	friendlyCave = random.randint(1,2)

	if chooseCave == str(friendlyCave):
		print('и делится с вами своии сокровищами!')
	else:
		print('...моментально вас съедает!')	
	print()
		
# main programm:

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)

	print('Попытаете удачу еще раз? (yes или no)')
	playAgain = input()