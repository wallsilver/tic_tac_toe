class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3 # Размер поля

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def check_win(self, player):
        # Проверка по горизонталям и вертикалям
        for i in range(self.field_size):
            if (all([self.board[i][j] == player for j in range(self.field_size)]) or
                    all([self.board[j][i] == player for j in range(self.field_size)])):
                return True

        # Проверка по диагоналям
        if (all([self.board[i][i] == player for i in range(self.field_size)]) or
                all([self.board[i][self.field_size - 1 - i] == player for i in range(self.field_size)])):
            return True

        return False

    def is_board_full(self):
        for row in range(self.field_size):
            for column in range(self.field_size):
                if self.board[row][column] == ' ':
                    return False
        return True

    # Переопределяем метод __str__.
    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        ) 