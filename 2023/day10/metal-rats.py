"""
Day 10

Strategy: Recursion

Go up,down,left,right from S to get potential paths
from there keep finding next step until back at start
Should end up with 2 paths

len(path) // 2 + 1 => furthest point away

Part 2:

- Find all connected sections using flood-fill
- For each connected section determine if section is enclosed
- To determine if the section is enclosed
    > Get first point
    > Count number of vertial pipes to the left (only going either up or down)
    > If the count is odd, its enclosed
- If enclosed add the length of the section to the area
"""

import sys

# Update recursion limit
sys.setrecursionlimit(100000)

tiles = []
x = 0
y = 0
with open('in.txt') as f:
    for line in f.read().split('\n'):
        if not line:
            continue
        tiles.append([])
        x = 0
        for tile in line:
            tiles[y].append(tile)
            if tile == 'S':
                start_pos = (y, x)
            x += 1
        y += 1

ALLOWED_NEXT_GOING_LEFT = ['-', 'L', 'F', 'S']
ALLOWED_NEXT_GOING_RIGHT = ['-', 'J', '7', 'S']
ALLOWED_NEXT_GOING_UP = ['|', '7', 'F', 'S']
ALLOWED_NEXT_GOING_DOWN = ['|', 'L', 'J', 'S']

def find_next_step(tile_map, y, x, prevY, prevX):
    """ Return the next step in the path """

    if x > len(tile_map[0])-1 or x < 0:
        return None

    if y > len(tile_map)-1 or y < 0:
        return None

    tile = tile_map[y][x]
    prev_tile = tile_map[prevY][prevX]
    
    if tile == '|':
        if (prevY == y-1 and prevX == x) and prev_tile in ALLOWED_NEXT_GOING_UP:
            return (y+1, x)
        elif (prevY == y+1 and prevX == x) and prev_tile in ALLOWED_NEXT_GOING_DOWN:
            return (y-1, x)

    if tile == '-':
        if (prevY == y and prevX == x-1) and prev_tile in ALLOWED_NEXT_GOING_LEFT:
            return (y, x+1)
        elif (prevY == y and prevX == x+1) and prev_tile in ALLOWED_NEXT_GOING_RIGHT:
            return (y, x-1)

    if tile == 'L': 
        if (prevY == y-1 and prevX == x) and prev_tile in ALLOWED_NEXT_GOING_UP:
            return (y, x + 1)
        elif (prevY == y and prevX == x+1) and prev_tile in ALLOWED_NEXT_GOING_RIGHT:
            return (y-1, x)

    if tile == 'J':
        if (prevY == y-1 and prevX == x) and prev_tile in ALLOWED_NEXT_GOING_UP:
            return (y, x-1)
        elif (prevY == y and prevX == x-1) and prev_tile in ALLOWED_NEXT_GOING_LEFT:
            return (y-1, x)

    if tile == '7':
        if (prevY == y and prevX == x-1) and prev_tile in ALLOWED_NEXT_GOING_LEFT:
            return (y+1, x)
        elif (prevY == y+1 and prevX == x) and prev_tile in ALLOWED_NEXT_GOING_DOWN:
            return (y, x-1)

    if tile == 'F':
        if ( prevY == y and prevX == x+1) and prev_tile in ALLOWED_NEXT_GOING_RIGHT:
            return (y+1, x)
        elif (prevY == y + 1 and prevX == x) and prev_tile in ALLOWED_NEXT_GOING_DOWN:
            return (y, x+1)

    # Invalid
    return None

def get_path(tile_map, y, x, visited, path):
    """ Recursively find the path """
    if (y, x) in visited:
        return

    if x > len(tiles[0])-1 or x < 0:
        return

    if y > len(tiles)-1 or y < 0:
        return

    if (x == start_pos[1] and y == start_pos[0]):
        return
    
    visited.append((y, x))
    path.append((y, x))
    
    for nextX, nextY in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
        if (nextY, nextX) in path:
            continue

        if next_step := find_next_step(tile_map, nextY, nextX, y, x):
            path.append((nextY, nextX))
            get_path(tile_map, next_step[0], next_step[1], visited, path)

def flood_fill(path, y, x, visited):
    """ Standard flood fill - find connected areas"""
    if (y, x) in path or (y, x) in visited:
        return
    
    if x > len(tiles[0])-1 or x < 0:
        return

    if y > len(tiles)-1 or y < 0:
        return
    
    visited.append((y, x))
    
    flood_fill(path, y, x+1, visited)
    flood_fill(path, y+1, x, visited)
    flood_fill(path, y-1, x, visited)
    flood_fill(path, y, x-1, visited)

# Determine paths by checking Up, Down, Left and Right from the start
paths = []
start_y, start_x = start_pos
for nextX, nextY in ((start_x+1, start_y), (start_x, start_y+1), (start_x-1, start_y), (start_x, start_y-1)):
    step = find_next_step(tiles, nextY, nextX, start_y, start_x)
    if step:
        path = []
        get_path(tiles, nextY, nextX, [], path)
        paths.append(path)

# Part 1
# print(len(paths[0]) // 2 + 1)

# Part 2
path = paths[0]
path.append((start_y, start_x))

# Find all connected sections
sections = []
for y in range(len(tiles)):
    for x in range(len(tiles[0])):
        skip = False
        for secs in sections:
            if (y, x) in secs:
                skip = True
                break
        if skip:
            continue

        sec = []
        flood_fill(path, y, x, sec)
        sections.append(sec)

# Check sections are enclosed: if enclosed add # of points to area
area = 0
for sec in sections:
    if not sec:
        continue
    left_path_count = 0
    y, x = sec[0]
    for px in range(x, -1, -1):
        if (y, px) in path and tiles[y][px] in ALLOWED_NEXT_GOING_UP:
            left_path_count += 1

    if not left_path_count % 2 == 0:
        area += len(sec)

print(area)
