# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?



# я сделала игру для людей, которые не просчитывают, сколько нужно забрать конфет с первого раза, чтобы выиграть. 
# не делала проверку на количество конфет, взятых игроком, т.к.будете долго код проверять)

from pickle import TRUE

number = 2021

while number > 28:
    n = int(input("Player 1, please take no more that 28 sweets: "))  
    number = number - n
    print(f"{number} sweets are left ")
    if number <= 28:
        print('Pleayer 2 you won!')
        break
    n = int(input("Player 2, please take no more that 28 sweets: "))
    number = number - n
    print(f"{number} sweets are left ")
    if number <= 28:
        print('Pleayer 1 you won!')
        break
    



