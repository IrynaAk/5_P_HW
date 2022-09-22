# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

# b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать 29 конфет, 
# то он, однозначно, проиграет. Достаточно довести игру до такой ситуации.

from pickle import TRUE
import random

number = 2021

while number > 28:
    n = int(input("Player, please take no more that 28 sweets: "))  
    number = number - n
    print(f"{number} sweets are left ")
    if number <= 28:
        print('Player, you lose!')
        break
    if number >= 30 and number <= 58:     # я добавила только проверку на последних шагах, если можно сделать 
                                          # так, чтобы игроку досталось 29 конфет на последнем ходе, бот так и делает
        n = number - 29
    else:
        n = random.randint(1, min(28,number))
    number = number - n
    print(f"Bot: {n} sweets are taken, {number} sweets are left ")
    if number <= 28:
        print('Pleayer, you won!')
        break
    




