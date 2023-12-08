"""
Brute force appraoch

Takes too long
"""

from itertools import repeat

file = 'in.txt'

def check_paths_end_with(paths, ch):
    for p in paths:
        if p[-1] != ch:
            return False
    return True

with open(file) as f:
    instructions, *values = [line for line in f.read().split('\n') if line != '']
    nodes = {}
    starting_paths = []
    ending_paths = []
    for n in values:
        node, path = n.split(' = ')
        path = [p.replace(')', '').replace('(', '') for p in path.split(', ')]
        nodes[node] = path
        if check_paths_end_with([node], 'A'):
            starting_paths.append(node)
        
        if check_paths_end_with([node], 'Z'):
            ending_paths.append(node)

    steps = 0
    cur_node = 'AAA'
    finish = False
    for _ in repeat(instructions):
        for ch in instructions:
            if check_paths_end_with(starting_paths, 'Z'):
                finish = True
                break
            idx = 0 if ch == 'L' else 1
            for i, p in enumerate(starting_paths):
                starting_paths[i] = nodes[p][idx]  

            steps += 1

        if finish:
            break

    print(steps)