"""Symbols module"""
import copy

class Symbols :
    """main symbols class"""
    elements_list = [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]]

    def check_win(self):
        """check win func, возвращает string "x"/"0", если победа, False, если проигрыш"""
        elements_list_len = len(self.elements_list)
        # check row win
        for i in range(elements_list_len):
            iterator = 0
            for j in range(elements_list_len):
                if self.elements_list[i][j] == self.elements_list[i][0] and self.elements_list[i][j] != " ":
                    iterator += 1
            if iterator == 3:
                return self.elements_list[0][0]

        # check column win
        for j in range(elements_list_len):
            iterator = 0
            for i in range(elements_list_len):
                if self.elements_list[i][j] == self.elements_list[0][j] and self.elements_list[i][j] != " ":
                    iterator += 1
            if iterator == 3:
                return self.elements_list[0][j]

        iterator = 0
        # check win by main diagonal
        for i in range(elements_list_len):
            if self.elements_list[i][i] == self.elements_list[0][0] and self.elements_list[i][i] != " ":
                iterator += 1
        if iterator == 3:
            return self.elements_list[0][0]

        # check win by side diagonal
        iterator = 0
        elements_list = copy.copy(self.elements_list)
        elements_list.reverse()
        for i in range(elements_list_len):
            if elements_list[i][i] == elements_list[0][0] and  elements_list[i][i] != " ":
                iterator += 1
        if iterator == 3:
            return elements_list[0][0]
        return False

    def fulling(self, cord_x, cord_y, sign) -> bool:
        """Fulling func, cord_x - координата, номер строки, cord_y - координата, номер столбца,
         sign - знак(X/O), возвращает False если успешно заполнено, True - индекс элемента занят"""
        busy = "This cell is occupied! Choose another one!"
        elements_lits_len = len(self.elements_list)
        for i in range(elements_lits_len):
            for j in range(elements_lits_len):
                if i == cord_x and j == cord_y:
                    if self.elements_list[i][j] != " ":
                        print(busy)
                        return True
                    self.elements_list[i][j] = sign

        symbol = f"""
        ┌─────┬─────┬─────┐
        │  {self.elements_list[0][0]}  │  {self.elements_list[0][1]}  │  {self.elements_list[0][2]}  │
        ├─────┼─────┼─────┤
        │  {self.elements_list[1][0]}  │  {self.elements_list[1][1]}  │  {self.elements_list[1][2]}  │
        ├─────┼─────┼─────┤
        │  {self.elements_list[2][0]}  │  {self.elements_list[2][1]}  │  {self.elements_list[2][2]}  │
        └─────┴─────┴─────┘
        """
        print(symbol)
        return False

symbols = Symbols()
