"""Table module"""
from symbols import symbols

class TicTactToe:
    """main class"""
    def __init(self):
        self.player = "X"

    def lobby(self):
        """Lobby func, запускается сначала"""
        print("TicTacToe by Maks")
        symbols.fulling(0, 0, " ")
        self.game_play()

    def change_player(self):
        """"Меняет значение Player, в зависимости от игрока ничего не возврвщает"""
        if self.player == "X":
            self.player = "0"
        elif self.player == "0":
            self.player = "X"

    def my_input(self):
        """Input координат пользователя для хода, возвращает координаты"""
        while True:
            if self.player == "X":
                new_player = "Player 0"
            else:
                new_player = "Player 1"

            try:
                cord_x, cord_y = input(f"{new_player}, Enter your index: ").split()
                cord_x, cord_y = int(cord_x), int(cord_y)
                cord_x -= 1
                cord_y -= 1
                if cord_x in range(0, 3) and cord_y in range(0, 3):
                    return cord_x, cord_y
            except ValueError:
                print("You should enter numbers!")

    def game_play(self):
        """Main func"""
        for i in range(9):
            i += 1
            iterator = True
            while iterator:
                cord_x, cord_y = self.my_input()
                iterator = self.fulling(cord_x, cord_y)

            if symbols.check_win() == "X" or symbols.check_win() == "0":
                print(f"{self.player}  Won!")
                break
            self.change_player()

    def fulling(self, cord_x, cord_y) -> bool:
        """Заполнение поля, cord_x - координата, номер строки, cord_y - координата, номер столбца,
         возвращает bool"""
        symbols_fulling_result = symbols.fulling(cord_x, cord_y, self.player)
        return symbols_fulling_result


tictactoe = TicTactToe()

# Точка входа
tictactoe.lobby()
