"""
Day 15 :D

boxes[hash(label)] = [(label, focus power), ...]
Manage boxes based on them rules

Reindeer lens logistics
"""

from collections import defaultdict


def get_focus_powers(boxes):
    focus_power = 0
    for k, box in boxes.items():
        focus_power += sum([(k+1) * (i+1) * lens[1] for i, lens in enumerate([b for b in box if b is not None])])
    return focus_power

def shuffle_boxes(boxes, h, i):
    """Shuffle boxes below i into next position"""
    for j in range(i, 0, -1):
        boxes[h][j] = boxes[h][j-1]
    boxes[h][0] = None

def sort_boxes(input: str, boxes):
    """from an input label perform the operation and manage boxes"""
    # Plus operation
    if '=' in input:
        label, focal_len = input.split('=')
        h = hash(label)
        found = False
        for i, val in enumerate(boxes[h]):
            if val and val[0] == label:
                boxes[h][i] = (label, int(focal_len))
                found = True
                break

        if not found:
            boxes[h].append((label, int(focal_len)))

    # Minus operation
    elif '-' in input:
        op = '-'
        label = input.split('-')[0]
        h = hash(label)
        for i, val in enumerate(boxes[h]):
            if val and val[0] == label:
                shuffle_boxes(boxes, h, i)



def hash(label: str) -> int:
    """Calculate the hash value for the input label"""
    curr_val = 0
    for c in label:
        curr_val += ord(c)
        curr_val *= 17
        curr_val %= 256
    
    return curr_val


if __name__ == "__main__":
    with open('in.txt') as f:
        init = f.read().split(',')
    
    boxes = defaultdict(list)

    # Part 1
    print('Part 1:', sum(hash(s) for s in init))

    # Part 2
    for s in init:
        sort_boxes(s, boxes)

    print('Part 2:', get_focus_powers(boxes))