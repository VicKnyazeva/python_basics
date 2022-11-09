# задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# а) Подумайте как наделить бота ""интеллектом""

import os
from random import randint

CANDIES_ON_START = 2021
MOVE_MAX_CANDIES = 28

# ----------------


def move_player(name, candies, max_move):
    while True:
        move = input(f'{name}, Ваш ход... ')
        try:
            move = int(move)
            if move > 0 and move <= max_move and move <= candies:
                return move
            else:
                print(
                    f'Количество взятых конфет должно быть в интервале от 1 до {max_move}')
        except:
            print('Необходимо ввести целое число.')


def move_stupid_bot(name, candies, max_move):
    move = randint(1, max_move) if candies >= max_move else randint(1, candies)
    return move


def move_smart_bot(name, candies, max_move):
    move = candies % (max_move + 1)
    if move == 0:
        move = randint(1, max_move) if candies >= max_move else candies
    return move


def play_game(
        player1_name, player1_move,
        player2_name, player2_move,
        candies, max_move):

    print(f'Осталось {candies} конфет')

    names = [player1_name, player2_name]
    moves = [player1_move, player2_move]

    player = randint(0, 1)

    while True:
        current_max_move = max_move if candies > max_move else candies
        name = names[player]
        move = moves[player](name, candies, current_max_move)

        candies -= move

        if candies == 0:
            print(f'{name} забрал последние конфеты')
            print(f'\n{name} - победитель!')
            break
        else:
            print(f'{name} забрал {move} конфет')
            print(f'\nОсталось {candies} конфет')

        player = (player + 1) % 2


# ------------------

os.system('cls')

game_type = input(
    'Введите: 0, если хотите играть с другим игроком,\n' +
    '         1, если хотите играть с глупым ботом,\n' +
    '        ... или любую другую цифру, если с умным...\n' +
    '> ')

player1_move = move_player

if game_type == '0':
    player1_name = input('Введите имя первого игрока: ')
    player2_name = input('Введите имя второго игрока: ')
    player2_move = move_player
else:
    player1_name = input('Введите свое имя: ')
    if game_type == '1':
        player2_name = 'Бот №1'
        player2_move = move_stupid_bot
    else:
        player2_name = 'Бот №2'
        player2_move = move_smart_bot

play_game(player1_name, player1_move,
          player2_name, player2_move,
          CANDIES_ON_START, MOVE_MAX_CANDIES)