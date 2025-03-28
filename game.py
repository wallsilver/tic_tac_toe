from Gameparts import Board
from Gameparts import FieldIndexError, CellOccupiedError


def save_results(self, result):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    game.display()
    # Тут пользователь вводит координаты ячейки.
    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: ')) - 1
                column = int(input('Введите номер столбца: ')) - 1
                if row < 0 or row >= game.field_size or column < 0 or column >= game.field_size:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError

            except FieldIndexError:
                #выводятся сообщения...
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue

                # Если в блоке try исключения не возникло...

            except ValueError:
                #выводятся сообщения...
                print(
                    'Буквы вводить нельзя. Только числа. '
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue

                # Если в блоке try исключения не возникло...
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue

            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break

        # В метод make_move передаются те координаты, которые ввёл пользователь.
        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        if game.check_win(current_player):
            result = f'Победили {current_player}.'
            print(result)
            running = False
            save_results(result)
        elif game.is_board_full():
            result = 'Ничья!'
            running = False
            save_results(result)
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()