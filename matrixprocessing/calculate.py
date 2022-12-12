"""калькулятор скрипт"""
TRANSPORE_MATRIX_TEXT = """
    1. Main diagonal
    2. Side diagonal
    3. Vertical line
    4. Horizontal line
"""


class Calculate:
    """main class"""
    def add_matrices(self, matrix_1, matrix_2):
        """сложение двух матриц, matrix_1, matrix_2 - матрицы, которые надо сложить, функция
        возвращает многоуровевый список, представляющий собой матрицу"""
        new_matrix_1 = []
        new_matrix_2 = []

        for i in matrix_1:
            for j in i:
                new_matrix_1.append(j)
        for i in matrix_2:
            for j in i:
                new_matrix_2.append(j)
        index_1 = 0
        index_2 = 0
        for i in matrix_1:
            for j in i:
                matrix_1[index_1][index_2] += matrix_2[index_1][index_2]
                index_2 += 1
            index_2 = 0
            index_1 += 1
        return matrix_1

    def transposiion(self, matrix):
        """переворот матрицы(метод используется только для умножения), функция возвращает
        многоуровевый список, представляющий собой матрицу, matrix - переворчиваемая матрица"""
        new_matrix = []
        new_matrix_column = []
        rows_count = len(matrix)
        columns_count = len(matrix[0])
        for index_1 in range(columns_count):
            for index_2 in range(rows_count):
                new_matrix_column.append(matrix[index_2][index_1])
            new_matrix.append(new_matrix_column)
            new_matrix_column = []
        return new_matrix

    def multiply_matrices(self, matrix_1, matrix_2):
        """функция умножения матриц, matrix_1, matrix_2 - матрицы, которые надо умножить,
         функция возвращает многоуровевый список, представляющий собой матрицу"""
        matrix_1 = self.transposiion(matrix_1)
        new_matrix_column = []
        new_matrix = []
        final_count = 0
        for index_3 in range(len(matrix_1[0])):
            for index_2 in range(len(matrix_2[0])):
                for index_1 in range(len(matrix_1[0])):
                    final_count += matrix_1[index_1][index_3]*matrix_2[index_1][index_2]
                new_matrix_column.append(final_count)
                final_count = 0
            new_matrix.append(new_matrix_column)
            new_matrix_column = []
        return new_matrix

    def multiply_matrix_by_const(self, matrix, const):
        """функция умножения матрицы на константу, matrix - матрица, const - константа,
        функция возвращает многоуровевый список, представляющий собой матрицу"""
        matrix_len = len(matrix)
        for index_1 in range(matrix_len):
            for index_2 in range(len(matrix[0])):
                matrix[index_1][index_2] *= const
        return matrix

    def transpore_matrix(self, matrix, __bool__):
        """функция транспонування матрицы, __bool__- если True, то сработает просто main_diagonal(),
        возвращает многоуровневый список, представляющий собой матрицу"""
        matrix_len = len(matrix)
        def main_diagonal(matrix):
            new_matrix = []
            new_matrix_column = []
            for index_1 in range(len(matrix[0])):
                for index_2 in range(matrix_len):
                    new_matrix_column.append(matrix[index_2][index_1])
                new_matrix.append(new_matrix_column)
                new_matrix_column = []
            return new_matrix

        def side_diagonal(matrix):
            matrix.reverse()
            for i in range(matrix_len):
                matrix[i].reverse()
            new_matrix = []
            new_matrix_column = []
            for index_1 in range(len(matrix[0])):
                for index_2 in range(matrix_len):
                    new_matrix_column.append(matrix[index_2][index_1])
                new_matrix.append(new_matrix_column)
                new_matrix_column = []
            return new_matrix

        def horizontal_line(matrix):
            matrix.reverse()
            return matrix

        def vertical_line(matrix):
            for i in range(matrix_len):
                matrix[i].reverse()
            return matrix

        if __bool__:
            matrix = main_diagonal(matrix)
        else:
            user_choice = input(f"{TRANSPORE_MATRIX_TEXT}> ")
            try:
                user_choice = int(user_choice)
            except ValueError:
                print("Введите целое число")
                self.transpore_matrix(matrix, False)
            else:
                if user_choice not in range(1, 5):
                    print("Введите число от 1 до 4")
                    self.transpore_matrix(matrix, False)
                else:
                    match user_choice:
                        case 1:
                            matrix = main_diagonal(matrix)
                        case 2:
                            matrix = side_diagonal(matrix)
                        case 3:
                            matrix = vertical_line(matrix)
                        case 4:
                            matrix = horizontal_line(matrix)
        return matrix

    def inverse_matrix(self, matrix):
        """Посчитать обратную матрицу, которую надо обернуть, возвращает матрицу"""
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix
        alliance_matrix = []
        for i in range(len(matrix)):
            matrix_height = []
            for j in range(len(matrix)):
                minor_symbol = (-1) ** (i + j)
                minor = self.get_minor(matrix, i, j)
                matrix_height.append(self.calculate_determinant(minor) * minor_symbol)
            alliance_matrix.append(matrix_height)
        main_determinant = self.calculate_determinant(matrix)

        inversed_matrix = self.multiply_matrix_by_const(alliance_matrix, 1/main_determinant)
        inversed_matrix = self.transpore_matrix(inversed_matrix, True)
        matrix_len = len(inversed_matrix)
        for i in range(matrix_len):
            for j in range(matrix_len):
                inversed_matrix[i][j] = round(inversed_matrix[i][j], 2)
                if inversed_matrix[i][j] == -0:
                    inversed_matrix[i][j] *= -1
                if inversed_matrix[i][j] % 10 == 0:
                    inversed_matrix[i][j] = round(inversed_matrix[i][j], 1)
                if inversed_matrix[i][j] % 100 == 0:
                    inversed_matrix[i][j] = round(inversed_matrix[i][j])

        return inversed_matrix

    def calculate_determinant(self, matrix):
        """посчитать определитель матрицы, возвоащает многоуровневый список, являющийся матрицей"""
        determinant = 0
        matrix_len = len(matrix)
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0]
        for i in range(matrix_len):
            minor_symbol = (-1) ** i
            minor = self.get_minor(matrix, i, 0)
            determinant += (self.calculate_determinant(minor) * minor_symbol * matrix[i][0])
        return determinant

    def get_minor(self, matrix, i, j):
        """Посчитать минор матрицы, matrix - та матрица, у которой считаем минор,
         i,j - координаты элемента, который вычеркиваем, возвращает лист с минором"""
        matrix_len = len(matrix)
        minor = []
        minor_cycled = []
        for index_1 in range(matrix_len):
            if index_1 == i:
                continue
            for index_2 in range(matrix_len):
                if index_2 == j:
                    continue
                minor_cycled.append(matrix[index_1][index_2])
            minor.append(minor_cycled)
            minor_cycled = []
        return minor

    def show_matrix(self, matrix):
        """"функция вывода матрицы в консоль, разбирает списки, и выводит их,
        ничего не возвращает, matrix - аргумент матрицы, которую надо вывести"""
        print("The Result is: ")
        matrix_str = ""
        for i in matrix:
            for j in i:
                if j % 1 == 0:
                    j = int(j)
                matrix_str += str(j) + " "
            matrix_str += "\n"
        print(matrix_str)

    def create_const(self):
        """функция инпута константы, возвращает константу"""
        user_const = input("Введите константу, на которую хотите умножить матрицу:\n> ")
        try:
            user_const = int(user_const)
        except ValueError:
            print("Введите целое число")
            self.create_const()
        return user_const

    def create_matrix(self):
        """функция создания матрицы, возвращает многоуровевый список, являющийся матрицей"""
        matrix = []
        cycle_var = True
        while cycle_var:
            matrix_size = input("Enter matrix size(AxB): > ")
            matrix = []
            try:
                matrix_size_list = matrix_size.split("x")
                matrix_row_count = matrix_size_list[0]
                matrix_column_count = matrix_size_list[1]
                matrix_column_count = int(matrix_size_list[1])
                matrix_row_count = int(matrix_size_list[0])
                cycle_var = False
            except ValueError:
                print("Enter an integer")

        if matrix_column_count in range(1, 11) and matrix_row_count in range(0, 11):
            row_list = []
            for index_0 in range(matrix_row_count):
                index_0 += 1
                while_var = True
                while while_var:
                    user_row = input("> ")
                    user_row_list = user_row.split(" ")
                    user_row_list_len = len(user_row_list)
                    if len(user_row_list) != matrix_column_count:
                        print("Неверный размер")
                        continue
                    try:
                        for index in range(user_row_list_len):
                            user_row_list[index] = float(user_row_list[index])
                    except ValueError:
                        print("Enter only numbers")
                    else:
                        while_var = False
                for index_5 in range(matrix_column_count):
                    row_list.append(user_row_list[index_5])
                matrix.append(row_list)
                row_list = []
        else:
            print("Enter an integer from 1 to 10")
            matrix = self.create_matrix()
        return matrix

    def check_col_row_equality(self, matrix_1, matrix_2) -> bool:
        """проверить равно ли количество колонок первой матрицы количеству рядком второй матрицы,
        matrix_1, matrix_2 - матрицы, которые сравниваются, возвращает True если равны,
        в ином случае - False, используется для умножения двух матриц"""
        if len(matrix_1) == 1:
            matrix_1_columns_count = 1
        else:
            matrix_1_columns_count = len(matrix_1[0])
        matrix_2_rows_count = len(matrix_2)
        if matrix_1_columns_count == matrix_2_rows_count:
            return True
        return False

    def check_is_square_matrix(self, matrix) -> bool:
        """проверяет квадратная ли матрица, возвращает True если квадратная, False - если нет
        matrix - проверяемая матрица"""
        if len(matrix) == len(matrix[0]):
            return True
        return False

    def check_equality(self, matrix_1, matrix_2) -> bool:
        """проверить равные ли по размеру матрицы, используется для сложения матриц,
        возврашает True, если равны, False - в ином случае"""
        matrix_1_rows = 0
        matrix_1_columns = 0
        matrix_2_rows = 0
        matrix_2_columns = 0
        for i in matrix_1:
            for j in i:
                j += 1
                matrix_1_columns += 1
            matrix_1_rows += 1
        for i in matrix_2:
            for j in i:
                matrix_2_columns += 1
            matrix_2_rows += 1
        if matrix_1_rows == matrix_2_rows and matrix_1_columns == matrix_2_columns:
            return True
        return False

calc = Calculate()
