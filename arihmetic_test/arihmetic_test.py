"""arihmetic test"""
import random
from datetime import datetime


class Arihmetic:
    """main class arihmetic"""
    FIRST_LVL = "simple operations with numbers 2-9"
    SECOND_LVL = "integral squares of 11-29"
    THIRD_LVL = "find the percentage of a number"
    START_TEXT = f"""Which level do you want? Enter a number:
    1 - {FIRST_LVL}
    2 - {SECOND_LVL}
    3 - {THIRD_LVL}
> """

    def input_user_choice(self) -> int:
        """Возвращает номер уровня, желаемого пройти пользователем"""
        while True:
            user_choice = input(self.START_TEXT)
            try:
                user_choice = int(user_choice)
            except ValueError:
                print("Enter an integer!")
            else:
                if user_choice in range(1, 4):
                    return user_choice
                print("There are only 3 levels!")

    def first_level(self):
        """1 урвоень, возвращает количество правильных ответов"""
        start_time = datetime.now()
        answer_count = 0
        for _ in range(5):
            number_1 = random.randrange(2, 10)
            number_2 = random.randrange(2, 10)
            operand = random.randrange(0, 4)
            match operand:
                case 0:
                    operator = "+"
                    answer = number_1 + number_2
                case 1:
                    operator = "-"
                    answer = number_1 - number_2
                case 2:
                    operator = "*"
                    answer = number_1 * number_2
                case 3:
                    operator = "/"
                    answer = number_1 / number_2

            iterator = True
            while iterator:
                user_answer = input(f"{number_1} {operator} {number_2} > ")
                try:
                    user_answer = float(user_answer)
                except ValueError:
                    print("Wrong format! Try again!")
                else:
                    if user_answer == answer:
                        print("Right!")
                        answer_count += 1
                    else:
                        print("Wrong!")
                    iterator = False
        time = datetime.now() - start_time
        return answer_count, time

    def second_level(self):
        """2 уровень, возврвщает количество правильных ответов"""
        start_time = datetime.now()
        answer_count = 0
        for _ in range(5):
            number_1 = random.randrange(11, 30)
            answer = number_1 ** 2
            print(number_1)
            iterator = True
            while iterator:
                user_answer = input("> ")
                try:
                    user_answer = int(user_answer)
                except ValueError:
                    print("Enter an integer!")
                else:
                    if user_answer == answer:
                        print("Right!")
                        answer_count += 1
                    else:
                        print("Wrong!")
                    iterator = False
        time = datetime.now() - start_time
        return answer_count, time

    def third_level(self):
        """3 уровень, возврвщает количество правильных ответов"""
        start_time = datetime.now()
        answer_count = 0
        for _ in range(5):
            number = random.randrange(1, 11) * 10
            percent = random.randrange(1, 11) * 10
            answer = number/100 * percent
            iterator = True
            while iterator:
                user_answer = input(f"{percent}% of {number} > ")
                try:
                    user_answer = int(user_answer)
                except ValueError:
                    print("Enter an integer!")
                else:
                    if user_answer == answer:
                        answer_count += 1
                        print("Right!")
                    else:
                        print("Wrong!")
                    iterator = False
        time = datetime.now() - start_time
        return answer_count, time

    def wants_save(self, answer_count, lvl_number, time):
        """Ничего не возврвщает, answer_count - количество правильных ответов,
        lvl_number - номер уровня, ничего не возврвщает"""
        choice = input(f"Your mark is {answer_count}/5. Would you like to save the result? Enter yes or no.\n> ")
        if choice.lower() == "yes" or choice.lower() == "y":
            self.save_file(answer_count, lvl_number, time)

    def save_file(self, answer_count, lvl_number, time):
        """функция записи правильных ответов в файл, ничего не возвращает,
        answer_count - количество правильных ответов, lvl_number - номер уровня"""
        time = str(time)[:7]
        user_name = input("What is your name?\n> ")
        file = open("results.txt", "w")
        saving_text = f"({time}) {user_name}: {answer_count}/5 in level {lvl_number}\n"
        file.write(saving_text)
        file.close()
        print('The results are saved in "results.txt".')


def main():
    """main func, ничего не возврвщает, не имеет аргументов"""
    arihmetic = Arihmetic()
    user_choice = arihmetic.input_user_choice()
    match user_choice:
        case 1:
            answer_count, time = arihmetic.first_level()
            arihmetic.wants_save(answer_count, f"1 ({arihmetic.FIRST_LVL}).", time)
            choice = input("Do you want to go to next level?(yes/no) > ")
            if choice.lower() == "yes":
                answer_count_lvl2, time = arihmetic.second_level()
                arihmetic.wants_save(answer_count_lvl2, f"2 ({arihmetic.SECOND_LVL}).", time)
                choice = input("Do you want to go to next level?(yes/no) > ")
                if choice.lower() == "yes":
                    answer_count_lvl3, time = arihmetic.third_level()
                    arihmetic.wants_save(answer_count_lvl3, f"3 ({arihmetic.THIRD_LVL})", time)
        case 2:
            answer_count, time = arihmetic.second_level()
            arihmetic.wants_save(answer_count, f"2 ({arihmetic.SECOND_LVL})", time)
            choice = input("Do you want to go to next level?(yes/no) > ")
            if choice.lower() == "yes":
                answer_count_lvl3, time = arihmetic.third_level()
                arihmetic.wants_save(answer_count_lvl3, f"3 ({arihmetic.THIRD_LVL})", time)

        case 3:
            answer_count_lvl3, time = arihmetic.third_level()
            arihmetic.wants_save(answer_count_lvl3, f"3 ({arihmetic.THIRD_LVL})", time)


def lobby():
    """start func"""
    print("Arihmetic Test by Maks")
    main()


if __name__ == "__main__":
    lobby()
