
def grid():
    global new_grid
    global new_grid_print
    global count
    if move in new_grid:
        count += 1
        if count % 2 == 0:
            new_grid = [i if i != move else 'O' for i in new_grid]
        else:
            new_grid = [i if i != move else 'X' for i in new_grid]

    new_grid_print = [i if i == 'X' or i == 'O' else " " for i in new_grid]

    print('---------')
    print('|', new_grid_print[0], new_grid_print[1], new_grid_print[2], '|')
    print('|', new_grid_print[3], new_grid_print[4], new_grid_print[5], '|')
    print('|', new_grid_print[6], new_grid_print[7], new_grid_print[8], '|')
    print('---------')



def game_state():
    check = [new_grid_print[0:3], new_grid_print[3:6], new_grid_print[6:9], new_grid_print[0:7:3],
             new_grid_print[1:8:3], new_grid_print[2:9:3], new_grid_print[0:9:4], new_grid_print[2:7:2],
             new_grid_print[0:4:7], new_grid_print[1:5:8], new_grid_print[2:6:9]]
    #print(check)
    global complete
    empty_cells = 'YES' if " " in new_grid_print else 'NO'

    difference = new_grid_print.count('X') - new_grid_print.count('O') \
        if new_grid_print.count('X') >= new_grid_print.count('O') \
        else new_grid_print.count('O') - new_grid_print.count('X')

    if ['X', 'X', 'X'] in check and ['O', 'O', 'O'] in check or difference >= 2:
        print('Impossible')
        complete = True
    elif ['X', 'X', 'X'] not in check and ['O', 'O', 'O'] not in check and empty_cells == 'YES':
        print('Game not finished')
    elif ['X', 'X', 'X'] not in check and ['O', 'O', 'O'] not in check and empty_cells == 'NO':
        print('Draw')
        complete = True
    elif ['X', 'X', 'X'] in check:
        print('X wins')
        complete = True
    elif ['O', 'O', 'O'] in check:
        print('O wins')
        complete = True


def user_move():
    global move

    numbers = [str(i) for i in range(10)]

    global cell_coordinates

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
symbols = "         "
cell_coordinates = [[first_cell[i], second_cell[i]] for i in range(9) if symbols[i] != ' ']
new_grid = [[first_cell[i], second_cell[i]] if symbols[i] == ' ' else symbols[i] for i in range(9)]
move = str()
complete = False
count = 0
new_grid_print = []
grid()
while not complete:
    user_move()
    grid()
    game_state()


