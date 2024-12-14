# Word search

file = 'in.txt'

words = []
with open(file) as f:
    for line in f.readlines():
        if line.strip():
            words.append(line.strip())

"""
Approach:

For every occurence of the letter 'X' search all directions for the word XMAS 
"""
#      (y, x)
LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)
DIAG_RIGHT_DOWN = (1, 1)
DIAG_RIGHT_UP = (-1, 1)
DIAG_LEFT_DOWN = (1, -1)
DIAG_LEFT_UP = (-1, -1)

"""
Recursively finds if a word is written in a given direction
Returns: 1 if word exists else 0
"""
def find_word_at(y, x, count, direction, word, words):
    if count >= len(word):
        return 1

    if y < 0 or y >= len(words) or x < 0 or x >= len(words[0]):
        return 0

    if words[y][x] != word[count]:
        return 0

    return find_word_at(y + direction[0], x + direction[1], count+1, direction, word, words)

def part_1():
    total = 0
    for y, line in enumerate(words):
        for x, char in enumerate(line):
            if char == 'X':
                total += sum([
                    find_word_at(y, x, 0, LEFT, "XMAS", words),
                    find_word_at(y, x, 0, RIGHT, "XMAS", words),
                    find_word_at(y, x, 0, UP, "XMAS", words),
                    find_word_at(y, x, 0, DOWN, "XMAS", words),
                    find_word_at(y, x, 0, DIAG_RIGHT_DOWN, "XMAS", words),
                    find_word_at(y, x, 0, DIAG_RIGHT_UP, "XMAS", words),
                    find_word_at(y, x, 0, DIAG_LEFT_DOWN, "XMAS", words),
                    find_word_at(y, x, 0, DIAG_LEFT_UP, "XMAS", words),
                ])
    print(total)

"""
Part 2:

For every A we come across search for the first MAS then for the other MAS
in either forwards or backwards direction

4 Cases for the starting cross (First 'M')
top left
top right
bottom left
bottom right
"""

def part_2():
    total = 0
    for y, line in enumerate(words):
        for x, char in enumerate(line):
            if char == 'A':
                # Search from first A starting top left
                start_y = y-1
                start_x = x-1
                cross_a = find_word_at(start_y, start_x, 0, DIAG_RIGHT_DOWN, "MAS", words)
                cross_b = find_word_at(start_y+2, start_x, 0, DIAG_RIGHT_UP, "MAS", words)
                cross_c = find_word_at(start_y, start_x+2, 0, DIAG_LEFT_DOWN, "MAS", words)
                if cross_a and (cross_b or cross_c):
                    total += 1
                    continue

                # bottom left
                start_y = y+1
                start_x = x-1
                cross_a = find_word_at(start_y, start_x, 0, DIAG_RIGHT_UP, "MAS", words)
                cross_b = find_word_at(start_y-2, start_x, 0, DIAG_RIGHT_DOWN, "MAS", words)
                cross_c = find_word_at(start_y, start_x+2, 0, DIAG_LEFT_UP, "MAS", words)
                if cross_a and (cross_b or cross_c):
                    total += 1
                    continue

                # bottom right
                start_y = y+1
                start_x = x+1
                cross_a = find_word_at(start_y, start_x, 0, DIAG_LEFT_UP, "MAS", words)
                cross_b = find_word_at(start_y, start_x-2, 0, DIAG_RIGHT_UP, "MAS", words)
                cross_c = find_word_at(start_y-2, start_x, 0, DIAG_LEFT_DOWN, "MAS", words)
                if cross_a and (cross_b or cross_c):
                    total += 1
                    continue

                # top right
                start_y = y-1
                start_x = x+1
                cross_a = find_word_at(start_y, start_x, 0, DIAG_LEFT_DOWN, "MAS", words)
                cross_b = find_word_at(start_y, start_x-2, 0, DIAG_RIGHT_DOWN, "MAS", words)
                cross_c = find_word_at(start_y+2, start_x, 0, DIAG_LEFT_UP, "MAS", words)

                if cross_a and (cross_b or cross_c):
                    total += 1
                    continue

    print(total)

part_2()
