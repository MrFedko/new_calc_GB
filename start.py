# Запускает программу, указывая на точку выхода после совершения высисления.
# Не взаимодействует с вычислениями, а только принимает значения от UI

from ui_calc import *
from commands import *

def start():
    while True:
        user_enter = from_user()
        result = product(user_enter)
        message = user_result(user_enter, result)
        print(message)
        action = input('Завершить программу? Y/N ').lower()
        if action == 'y':
            break
        
if __name__ == '__main__':
    start()