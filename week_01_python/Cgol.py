import sys, time

def create_new_board(rows, cols):
    a = []
    for i in range(rows):
        a.append([])
        for j in range(cols):
            # a[i][j] = '-'
            a[i].append('-')
    return a

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = '')
        print('')
    print('')


def set_cell(board, r, c, val):
    board[r][c] = val

def count_neighbors(board, r, c):
    living_neighbors = 0
    i = r-1
    for i in range(r-1, r+2): # from one row before to another
        if(i >= 0 and i < len(board)): # within row bounds
            j = c-1
            for j in range(c-1, c+2): # from one column before to one after
                if(j >= 0 and j < len(board[r])): # within column bounds
                    if(board[i][j] == 'X'): # cell is alive
                        living_neighbors = living_neighbors + 1 # add to living_neighbors
    if(board[r][c] == 'X'): # if current cell alive...
        living_neighbors = living_neighbors - 1 # ...it's not a 'neighbor'
    return living_neighbors

def get_next_gen_cell(board, r, c):
    next_gen_cell = '-' # default: dead stays dead
    if(board[r][c] == 'X'): # for a space that is populated:
        # Each cell with one or no neighbors dies, as if by solitude.
        # Each cell with four or more neighbors dies, as if by overpopulation.
        # Each cell with two or three neighbors survives.
        if(count_neighbors(board, r, c) < 2 or count_neighbors(board, r, c) > 3):
            next_gen_cell = '-' # alive becomes dead
        else:
            next_gen_cell = 'X' # alive stays alive
    elif(count_neighbors(board, r, c) == 3): # already know it's not populated
        next_gen_cell = 'X' # Each cell with three neighbors becomes alive. (dead becomes alive)
    # only other possibility: dead stays dead
    return next_gen_cell

def generate_next_board(board):
    new_board = []
    for row in range(len(board)):
        new_board.append([])
        for cell in range(len(board[row])):
            new_board[row].append(get_next_gen_cell(board, row, cell))
    return new_board


###################################

board = create_new_board(10,10)
# print_board(board)

# breathe life into some cells:
# box around 4,4
set_cell(board, 3, 3, 'X')
set_cell(board, 3, 4, 'X')
set_cell(board, 3, 5, 'X')
set_cell(board, 4, 3, 'X')
set_cell(board, 4, 5, 'X')
set_cell(board, 5, 3, 'X')
set_cell(board, 5, 4, 'X')
set_cell(board, 5, 5, 'X')

# print_board(board)

###############################

for i in range(20):
    # sys.stdout.write('/-\\|'[i%4])
    print('Gen: ' + str(i))
    print_board(board)
    time.sleep(0.5)
    sys.stdout.write('\r')
    board = generate_next_board(board)