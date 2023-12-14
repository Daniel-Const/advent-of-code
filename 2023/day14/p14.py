from copy import deepcopy
from collections import Counter

directions = {
    'N': (-1, 0),
    'W': (0, -1),
    'S': (1, 0),
    'E': (0, 1)
}

def show(board, end="\n"):
    for b in board:
        print(b)
    print(end)

def move_north(board, row, col):
    """
    North: row - i - 1
    East: col - i - 1
    South: row + i + 1
    West: col + i + 1
    
    """
    i = 0
    while row-i-1 >= 0 and board[row-i-1][col] == '.':
        i += 1

    if i > 0:
        board[row-i][col] = 'O'
        board[row][col] = '.'

def move_rock(board, row, col, direction):
    i = 0
    r_inc, c_inc = direction
    r = row + (i * r_inc) + r_inc
    c = col + (i * c_inc) + c_inc
    while r >= 0 and c >= 0 and r < len(board) and c < len(board[0]) and board[r][c] == '.':
        # print(r ,' vs ', row - i - 1)
        i += 1
        r = row + (i * r_inc) + r_inc
        c = col + (i * c_inc) + c_inc
    
    # print('Done; i = ', i, '\n', board[r - r_inc][c - c_inc])
        
    if i > 0:
        board[r - r_inc][c - c_inc] = 'O'
        board[row][col] = '.'

 
def tilt(board, direction):
    new_board = deepcopy(board)
    dir_r, dir_c = direction

    if dir_r == 1:
        r_range = (len(new_board)-1, -1, -1)
    else:
        r_range = (0, len(new_board), 1)
    
    if dir_c == 1:
        c_range = (len(new_board[0])-1, -1, -1)
    else:
        c_range = (0, len(new_board[0]), 1)

    for r in range(*r_range):
        for c in range(*c_range):
            if new_board[r][c] == 'O':
                move_rock(new_board, r, c, direction)
    return new_board

def calculate_load(board):
    for i, row in enumerate(board):
        count = Counter(row)
        yield count['O'] * (len(row) - i)


def stringify(board):
    return ''.join(''.join([ch for ch in row]) for row in board)    

def get_first_cycle(board, start=0, iters=100):
    # board_states = {}
    # cycle_states = {}
    loads = []
    states = {}
    for i in range(iters):
        # Do a cycle
        for k in ('N', 'W', 'S', 'E'):
            board = tilt(board, directions[k])

        key = stringify(board)
        if key in states:
            return loads, i
        
        
        total_load = sum(calculate_load(board))
        if i > start:
            states[stringify(board)] = {'load': total_load, 'cycle': i}
            loads.append(total_load)


if __name__ == "__main__":
    with open('in.txt') as f:
        board = [[c for c in line if c != '\n'] for line in f.readlines()]
    
    # show(board, end="\n\n")
    iters = 1000000000
    _, offset = get_first_cycle(board, start=0, iters=iters)
    loads, idx = get_first_cycle(board, start=offset, iters=iters)
    # pattern_start = idx - offset - 1
    print('first pattern ends: ', offset)
    print('first pattern starts: ', offset - len(loads) + 1) # 'offset'
    print(len(loads))
    starts = offset - (len(loads))

    # print(loads)
    # print(offset, idx)
    l = len(loads)
    k = (l - (iters % l)) + (l % starts)
    print(k)
    """
    offset+1 = start of pattern
    idx - offset = len of pattern
    """

    # print(cycle_states)
    # k = len(cycle_states) - ((iters - offset) % len(cycle_states))
    # print(k+1)
    print(loads[k])

