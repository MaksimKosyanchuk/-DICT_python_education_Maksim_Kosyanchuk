"""import calculator module"""
from calculate import calc


class Matrixprocessing:
    """main class"""
    def __init__(self):
        START_TEXT = """
        1. Add matrices
        2. Multiply matrix by a constant
        3. Multiply matrices
        4. Transpose matrix
        5. Calculate a determinant
        6. Inverse matrix
        0. Exit
        """

    def input_user_choice(self) -> int:
        """Функция инпут выбора действия от пользователя, возвращает integer выбора пользователя"""
        while True:
            print(self.START_TEXT)
            user_choice_var = input("Your choice: > ")
            try:
                user_choice_var = int(user_choice_var)
                if user_choice_var in range(0, 7):
                    break
                print("enter integers from 0 to 6!\n")
            except ValueError:
                print("enter integers from 0 to 6!\n")
        return user_choice_var

    @staticmethod
    def check_user_choice(user_choice) -> bool:
        """сравниваем выбор пользователя  с доступными, user_choice - выбор пользователя,
         целое число от 0 до 6, делает операции в зависимости от выбора,
         возвращает False если надо завершить программу"""
        match user_choice:
            case 1:
                matrix_1 = calc.create_matrix()
                matrix_2 = calc.create_matrix()
                if calc.check_equality(matrix_1, matrix_2):
                    matrix = calc.add_matrices(matrix_1, matrix_2)
                    calc.show_matrix(matrix)
                else:
                    print("Cлаживать можно только равные по столбцам и колонкам матрицы")
            case 2:
                matrix = calc.create_matrix()
                const = calc.create_const()
                matrix = calc.multiply_matrix_by_const(matrix, const)
                calc.show_matrix(matrix)
            case 3:
                matrix_1 = calc.create_matrix()
                matrix_2 = calc.create_matrix()
                if calc.check_col_row_equality(matrix_1, matrix_2):
                    matrix = calc.multiply_matrices(matrix_1, matrix_2)
                    calc.show_matrix(matrix)
                else:
                    print("Size-error")
            case 4:
                matrix = calc.create_matrix()
                if calc.check_is_square_matrix(matrix):
                    matrix = calc.transpore_matrix(matrix, False)
                    calc.show_matrix(matrix)
                else:
                    print("Транспонувать можно только квадратные матрицы")
            case 5:
                matrix = calc.create_matrix()
                if calc.check_is_square_matrix(matrix):
                    determinant = calc.calculate_determinant(matrix)
                    print(f"Determinant: {determinant}")
                else:
                    print("Посчитать определить можно только у квадратных матриц")
            case 6:
                matrix = calc.create_matrix()
                if not calc.check_is_square_matrix(matrix):
                    print("Инвертировать можно только квадратные матрицы")
                else:
                    if calc.calculate_determinant(matrix) != 0:
                        matrix = calc.inverse_matrix(matrix)
                        calc.show_matrix(matrix)
                    else:
                        print("Error! Determinant = 0!")
            case 0:
                return False
        return True


matrix_proc = Matrixprocessing()


def main():
    """Main функция"""
    user_playment = True
    while user_playment:
        user_choice = matrix_proc.input_user_choice()
        user_playment = matrix_proc.check_user_choice(user_choice)


# Точка входа
main()