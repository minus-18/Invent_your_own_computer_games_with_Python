import random


def draw_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():
    letter = ''
    while not (letter in ('X', 'O')):
        print('Вы выбираете \'X\' или \'O\'?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Вы'
