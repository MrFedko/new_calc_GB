
def product(from_user_list):
    result = 0
    if from_user_list[1] == '+':
        result = from_user_list[0] + from_user_list[2]
    elif from_user_list[1] == '-':
        result = from_user_list[0] - from_user_list[2]
    elif from_user_list[1] == '*':
        result = from_user_list[0] * from_user_list[2]
    elif from_user_list[1] == '/':
        if from_user_list[2] == 0:
            print('Делить на ноль нельзя')
            exit()
        result = from_user_list[0] / from_user_list[2]
    elif from_user_list[1] == '**':
        result = from_user_list[0] ** from_user_list[2]
    return result
