# Принимает значения от пользователя, отправляет их в commands. 
# Затем принимает результат от commands и визуализирует его
from commands import *


def from_user():
    operators = ['+', '-', '/', '*', '**']
    first_number = float(input('Введите первое число: '))
    user_char = input('Оператор: ')
    while user_char not in operators:
        print('Неверный оператор')
        user_char = input('Оператор: ')        
    second_number = float(input('Введите второе число: '))
    
    return [first_number, user_char, second_number]

def user_result(list, result):
    message = f'{list[0]} {list[1]} {list[2]} = {result}'
    return message