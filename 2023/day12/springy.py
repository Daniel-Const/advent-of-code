"""
TODO: Part 2
"""

with open('in.txt') as f:
    lines = f.read().splitlines()
    records = []
    for line in lines:
        springs, groups = line.split(' ')
        records.append({
            'springs': springs,
            'groups': tuple(int(i) for i in groups.replace(',', ' ').split(' '))
        })

def is_record_valid(springs: str, groups: list[int]):
    count = 0
    counts = []
    for s in springs + '.':
        if s == '#':
            count += 1
        if s == '.':
            if count > 0:
                counts.append(count)
                count = 0
    return tuple(counts) == groups

# Part 2
def unfold(springs, groups):
    s = springs
    g = groups[:]
    for _ in range(4):
        s += f'?{springs}'
        g += groups
    
    return s, g

def get_arrangements(springs, groups):
    
    if '?' not in springs:
        return 1 if is_record_valid(springs, groups) else 0
    
    for i, s in enumerate(springs):
        if s == '?':
            right = f'{springs[:i]}.{springs[i+1:]}'
            left = f'{springs[:i]}#{springs[i+1:]}'
            return get_arrangements(right, groups) + get_arrangements(left, groups)

count = 0
for record in records:
    springs, groups = record['springs'], record['groups']
    # springs, groups = unfold(springs, groups)
    c = get_arrangements(springs, groups)
    # print(c)
    count += c

print(count)