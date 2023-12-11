"""
Strategy:

- Find all the rows and column numbers that have expansions in them
- Compare all galaxies to eachother
- Calculate galaxy-galaxy distance using Manhattan Distance.
- x_dist = x_dist + (expansison_factor - 1) * number of x expansions (same for y)
- (expansion_factor - 1) because we don't want to include the x's that we already counted in x_dist

General solution for part 1 and 2:
Part 1: Set EXPANSION_FACTOR = 2
Part 2: Set EXPANSION_FACTOR = 1000000
"""

EXPANSION_FACTOR = 2

image = []
with open('in.txt', 'r') as f:
    for line in f.readlines():
        image.append([ch for ch in line if ch != '\n'])

def find_expansions(image):
    r_expansions = []
    c_expansions = []
    for i, row in enumerate(image):
        if all(r == '.' for r in row):
           r_expansions.append(i)

    for c in range(len(image[0])):
        if all(image[r][c] == '.' for r in range(len(image))):
            c_expansions.append(c)

    return r_expansions, c_expansions 

r_exp, c_exp = find_expansions(image)

# Get all galaxy locations
galaxies = []
for r, row in enumerate(image):
    for c, col in enumerate(row):
        if image[r][c] == '#':
            galaxies.append((r, c))

# Calculate distances
distances = 0
for (from_r, from_c) in galaxies:
    for (to_r, to_c) in galaxies:
        c_dist = abs(from_c - to_c)
        r_dist = abs(from_r - to_r)

        distances += r_dist + len([r for r in r_exp if r in range(from_r, to_r, 1 if from_r < to_r else -1)]) * (EXPANSION_FACTOR-1)
        distances += c_dist + len([c for c in c_exp if c in range(from_c, to_c, 1 if from_c < to_c else -1)]) * (EXPANSION_FACTOR-1)

print(distances // 2)
