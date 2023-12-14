"""
Cycle detection!

When the board is in a state it was in previously, it will forever
repeat all the states in between

Find the length of the cycle and the # cycles remaining to get the load at
cycle x

|xxxx|
     |xxxx|
          |xxxx|
|------------|
|1234|1234|1234|
             ^
"""

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

def move_rock(board, row, col, direction):
    i = 0
    r_inc, c_inc = direction
    r = row + (i * r_inc) + r_inc
    c = col + (i * c_inc) + c_inc
    while r >= 0 and c >= 0 and r < len(board) and c < len(board[0]) and board[r][c] == '.':
        i += 1
        r = row + (i * r_inc) + r_inc
        c = col + (i * c_inc) + c_inc
            
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
        print(i, total_load)
        if i > start:
            states[stringify(board)] = {'load': total_load, 'cycle': i}
            loads.append(total_load)

    # No cycles
    return None


if __name__ == "__main__":
    with open('ex.txt') as f:
        board = [[c for c in line if c != '\n'] for line in f.readlines()]
    
    iters = 1000000000

    # Offset (+ 1) gives us the start of a cycle
    _, offset = get_first_cycle(board, start=0, iters=iters)
    
    # Starting from offset, get all the loads in the cycle
    loads, _ = get_first_cycle(board, start=offset, iters=iters)

    # Index into the loads => (remaining cycles) % length of cycle
    k = ((iters - offset - 1) % len(loads)) - 1
    print(loads[k])
