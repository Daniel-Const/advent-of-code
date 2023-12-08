"""
Better solution:

Track the number of steps for each starting point to get to an end
The solution is the Lowest Common Mulitple of all of these steps
"""

from itertools import repeat
from functools import reduce
import math

file = 'in.txt'

def check_path_ends_with(path, ch):
    return path[-1] == ch

with open(file) as f:
    instructions, *values = [line for line in f.read().split('\n') if line != '']
    nodes = {}
    starting_paths = []
    ending_paths = []
    for n in values:
        node, path = n.split(' = ')
        path = [p.replace(')', '').replace('(', '') for p in path.split(', ')]
        nodes[node] = path
        if check_path_ends_with(node, 'A'):
            starting_paths.append(node)
        
        if check_path_ends_with(node, 'Z'):
            ending_paths.append(node)

    steps = 1
    finish = False
    endings = [0 for _ in range(len(starting_paths))]
    for _ in repeat(instructions):
        for ch in instructions:
            idx = 0 if ch == 'L' else 1
            for i, p in enumerate(starting_paths):
                if p == None:
                    continue
                starting_paths[i] = nodes[p][idx]
                if check_path_ends_with(starting_paths[i], 'Z'):
                    endings[i] = steps
                    starting_paths[i] = None
                                            
            if all(p == None for p in starting_paths):
                finish = True
                break

            steps += 1

        if finish:
            break
    
    # Find the lowest common multiple of all endings
    print(reduce(math.lcm, endings))