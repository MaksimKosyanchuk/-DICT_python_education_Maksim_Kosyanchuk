"""random module"""
import random


def main(): #pylint: disable=R0912
    """main func"""
    friends_dict = {}
    friends_list = []

    while True:
        friends_count = input("Enter the number of friends joining (including you): ")
        try:
            friends_count = int(friends_count)
        except ValueError:
            print('Введите число')
            continue

        if friends_count < 1:
            print("No one is joining for the party")
            continue

        friends_list = first_filling_dict(friends_dict, friends_count, 0, friends_list)
        break

    while True:
        money_count = input("Enter the total amount: ")
        try:
            money_count = float(money_count)
        except ValueError:
            print('Введите число')
            continue

        if money_count <= 0:
            print("sum must be greater than 0")
        else:
            break

    cycle_var = True
    while cycle_var:
        answer_user = input("\nХотите выбрать счастливчика?(yes/no)\n>>")
        if answer_user == "yes":
            lucker = set_lucker(friends_count, friends_list)
            cycle_var = False
        elif answer_user == "no":
            lucker = "none"
            cycle_var = False
        else:
            print('Enter "yes" or "no" ')

    if lucker != "none":
        print(f"{lucker} is the lucky one!")
        money_count = division(friends_count-1, money_count)
    else:
        print("No one is going to be lucky")
        money_count = division(friends_count, money_count)

    filling_dict(friends_dict, money_count, friends_count, friends_list, lucker)


def set_lucker(friends_count, friends_list):
    """set luckher func"""
    lucker = random.randint(0, friends_count-1)
    lucker = friends_list[lucker]
    return lucker


def division(friends_count, money_count):
    """division money func"""
    money_count = money_count/friends_count
    money_count = round(money_count, 2)
    return money_count


def first_filling_dict(friends_dict, friends_count, money_count, friends_list):
    """firstly fulling dict"""
    print("\nEnter the name of every friend (including you), each on a new line: ")

    for index in range(friends_count):
        index += 1
        name = input(">> ")
        friends_list.append(name)
        friends_dict[name] = money_count
    return friends_list


def filling_dict(friends_dict, money_count, friends_count, friends_list, lucker):
    """fulling dict"""
    for index in range(friends_count):
        name = friends_list[index]
        if lucker != name:
            friends_dict[name] = money_count
        else:
            friends_dict[name] = 0
    print(friends_dict)


# Точка входа
main()
