"""chatbot"""
print("Hello! My name is Chat Bot\nI was created in 2022")
user_name = input("Please, remind me your name: ")

print(f"What a great name you have, {user_name}!")
print("Let me guess your age.\nEnter remainders of diving your age by 3,5 and 7.")

first_num = int(input())
second_num = int(input())
third_num = int(input())

USER_AGE = str((first_num * 70 + second_num * 21 + third_num * 15) % 105)

print(f"Your age is {USER_AGE}; that's a good time to start programming!")
user_num = int(input("Now I will prove to you that I can count to any number you want.\n"))

for value in range(user_num+1):
    print(str(value) + "!")
    value = value +1

print("Completed, have a nice day!")
print("Ok, now I give you test: ")
FIRST_QUESTION = """
Имеет ли Python динамический тип данных?(Ввести номер ответа)
1.Да
2.Нет
3.Не знаю
"""

print(FIRST_QUESTION)
user_first_answer = int(input())

SECOND_QUESTION = """
Обязательно ли функции в Python должны что-то возвращать?(Ввести номер ответа)
1.Да
2.Нет
3.Не знаю"
"""
print(SECOND_QUESTION)
user_second_answer = int(input())

while (user_first_answer != 1) or (user_second_answer != 2):
    print("Please, try again.")
    print(FIRST_QUESTION)
    user_first_answer = int(input())
    print(SECOND_QUESTION)
    user_second_answer = int(input())

print("Congratulations, have a nice day!")
