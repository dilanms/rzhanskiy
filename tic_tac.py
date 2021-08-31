def grid():
    new_grid = [[first_cell[i], second_cell[i]]
                if symbols[i] == ' ' else symbols[i] for i in range(9)]

    if move in new_grid:
        new_grid = [i if i != move else 'X' for i in new_grid]

    new_grid = [i if i == 'X' or i == 'O' else ' ' for i in new_grid]

    print('---------')
    print('|', new_grid[0], new_grid[1], new_grid[2], '|')
    print('|', new_grid[3], new_grid[4], new_grid[5], '|')
    print('|', new_grid[6], new_grid[7], new_grid[8], '|')
    print('---------')


def game_state():
    check = [symbols[0:3], symbols[3:6], symbols[6:9], symbols[0:7:3],
             symbols[1:8:3], symbols[2:9:3], symbols[0:9:4], symbols[2:7:2]]

    empty_cells = 'YES' if ' ' in symbols else 'NO'

    difference = symbols.count('X') - symbols.count('O') \
        if symbols.count('X') >= symbols.count('O') \
        else symbols.count('O') - symbols.count('X')

    if 'XXX' in check and 'OOO' in check or difference >= 2:
        print('Impossible')
    elif 'XXX' not in check and 'OOO' not in check and empty_cells == 'YES':
        print('Game not finished')
    elif 'XXX' not in check and 'OOO' not in check and empty_cells == 'NO':
        print('Draw')
    elif 'XXX' in check:
        print('X wins')
    elif 'OOO' in check:
        print('O wins')


def user_move():
    global move

    numbers = [str(i) for i in range(10)]

    cell_coordinates = [[first_cell[i], second_cell[i]] for i in range(9)
                        if symbols[i] != ' ']

    while True:
        move = input('Enter the coordinates: ').split()

        if move[0] not in numbers or move[1] not in numbers:
            print('You should enter numbers!')
        elif move[0] not in numbers[1:4] or move[1] not in numbers[1:4]:
            print('Coordinates should be from 1 to 3!')
        elif move in cell_coordinates:
            print('This cell is occupied! Choose another one!')
        else:
            cell_coordinates += [move]
            break


first_cell = ['1', '1', '1', '2', '2', '2', '3', '3', '3']
second_cell = ['1', '2', '3', '1', '2', '3', '1', '2', '3']

symbols = input('Enter cells: ').replace('_', ' ')
move = str()

grid()
user_move()
grid()
