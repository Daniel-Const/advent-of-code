import sys

sys.setrecursionlimit(900000)

file = 'test.txt'
board = []

#    (row, col)
UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

directions = (UP, RIGHT, DOWN, LEFT)

with open(file) as f:
    for line in f.readlines():
        board.append([l for l in line.strip()])

def find_guard_pos(board):
    for r, line in enumerate(board):
        for c, char in enumerate(board[r]):
            if char == '^':
                return r, c, 0
            elif char == '>':
                return r, c, 1
            elif char == 'v':
                return r, c, 2
            elif char == '<':
                return r, c, 3



def guard_step(board, dir, row, col):
    new_row = directions[dir][0] + row
    new_col = directions[dir][1] + col

    if new_row < 0 or new_col < 0 or new_row >= len(board) or new_col >= len(board[0]):
        return

    board[row][col] = 'X'
    if board[new_row][new_col] == '#':
        dir = (dir + 1) % 4
        return guard_step(board, dir, row, col)
    
    guard_step(board, dir, new_row, new_col)

def is_in_loop(board, dir, row, col):
    start_row = row
    start_col = col
    start_dir = dir
    while True:
        new_row = directions[dir][0] + row
        new_col = directions[dir][1] + col

        if new_row < 0 or new_col < 0 or new_row >= len(board) or new_col >= len(board[0]):
            return False

        if board[new_row][new_col] == '#':
            dir = (dir + 1) % 4
            new_row = row
            new_col = col

        row = new_row
        col = new_col

        if row == start_row and col == start_col and dir == start_dir:
            return True

def part_1():
    row, col, direction_idx = find_guard_pos(board)
    guard_step(board, direction_idx, row, col)
    count = 0
    for r in board:
        for c in r:
            if c == 'X':
                count += 1

    print(count+1)

# Not working atm...
def part_2():
    row, col, direction_idx = find_guard_pos(board)
    count = 0
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if board[r][c] == '#' or board[r][c] in ['^', '>', '<', 'v']:
                continue

            new_board = []
            for line in board:
                new_board.append([l for l in line])

            new_board[r][c] = '#'
            print(new_board)
            if is_in_loop(board, direction_idx, r, c):
                count += 1

    print(count)

part_2()

