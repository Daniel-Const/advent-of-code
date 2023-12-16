"""
Day 16 :D

lazer beams
"""

class Directions:
    def __init__(self):
        self.right = (0, 1)
        self.left = (0, -1)
        self.up = (-1, 0)
        self.down = (1, 0)

class Tile:
    def __init__(self, char):
        self.char = char
        self.energized = False

directions = Directions()

mirror_maps = {
    '/': {
        directions.right: directions.up,
        directions.left: directions.down,
        directions.up: directions.right,
        directions.down: directions.left
    },
    '\\': {
        directions.right: directions.down,
        directions.left: directions.up,
        directions.up: directions.left,
        directions.down: directions.right
    }
}


split_directions_vert =  [directions.right, directions.left]
split_directions_horiz = [directions.up, directions.down]

# Part 2
def get_start_beams(grid):

    beams = []
    # Traverse vertical edges
    for r in range(0, len(grid)):
        for c in [0, len(grid[0])-1]:
            beams.append((r, c, directions.left if c > 0 else directions.right))
            if r == 0:
                beams.append((r, c, directions.down))
            elif r == len(grid)-1:
                beams.append((r, c, directions.up))

    # Traverse horiz edges
    for c in range(0, len(grid[0])):
        for r in [0, len(grid)-1]:
            beams.append((r, c, directions.up if r > 0 else directions.down))
            if c == 0:
                beams.append((r, c, directions.right))
            elif c == len(grid[0])-1:
                beams.append((r, c, directions.left))


    return beams

def follow_beam(grid, beam_queue):
    visited = []
    energized = 0
    while len(beam_queue):
        r, c, d = beam_queue.pop()
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]):

            if (r, c, d) in visited:
                break

            if not grid[r][c].energized:
                grid[r][c].energized = True
                energized += 1

            tile = grid[r][c].char
            visited.append((r, c, d))
        
            if tile == '.':
                r += d[0]
                c += d[1]
                continue
            
            if tile == '-':
                if d in split_directions_horiz:
                    beam_queue.append((r, c+1, directions.right))
                    beam_queue.append((r, c-1, directions.left))
                    break

            if tile == '|':
                if d in split_directions_vert:
                    beam_queue.append((r+1, c, directions.down))
                    beam_queue.append((r-1, c, directions.up))
                    break
            
            # Get new direction
            if tile in mirror_maps:
                d = mirror_maps[tile][d]

            r += d[0]
            c += d[1]

    return energized


def show_grid(grid):
    for r in grid:
        print(''.join([t.char for t in r]))


def reset_grid(grid):
    for r in grid:
        for tile in r:
            tile.energized = False

if __name__== '__main__':
    file = 'ex.txt'
    grid = []
    max_count = 0
    with open(file) as f:
        for line in f.readlines():
            grid.append([Tile(c) for c in line if c != '\n'])

    queue = get_start_beams(grid)
    for q in queue:
        reset_grid(grid)
        count = follow_beam(grid, [q])
        if count > max_count:
            max_count = count

    print(max_count)