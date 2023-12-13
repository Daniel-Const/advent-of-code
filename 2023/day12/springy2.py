"""
Springs part 2
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


memo = {}

def get_arrangements(springs, groups, i, cur_group, cur_group_len):
    if (i, cur_group, cur_group_len) in memo:
        return memo[(i, cur_group, cur_group_len)]
    
    """
    Base case:
    At the end of the springs
    Valid if current group == length of groups
    Otherwise failed to match contiguous blocks
    """
    if i == len(springs):
        if cur_group == len(groups):
            return 1
        else:
            return 0
    
    def recurse(s):
        """Recursively search space: increment i and handle spring cases"""
        r = 0
        # Broken: increment current consecutive number
        if s == '#':
            r += get_arrangements(springs, groups, i+1, cur_group, cur_group_len+1)
        # Working: If previously on a contiguous group check it was valid - Increment current group
        elif s == '.' and cur_group_len > 0 and cur_group < len(groups) and cur_group_len == groups[cur_group]:
            r += get_arrangements(springs, groups, i+1, cur_group+1, 0)
        # Working: Just continue
        elif s == '.' and cur_group_len == 0:
            r += get_arrangements(springs, groups, i+1, cur_group, 0)
        return r
    
    result = 0
    if springs[i] == '?':
        result = recurse('#') + recurse('.')
    else:
        result = recurse(springs[i])

    # Cache result
    memo[(i, cur_group, cur_group_len)] = result
    return result

count = 0
for record in records:
    springs, groups = record['springs'], record['groups']
    print(springs)
    c = get_arrangements('?'.join([springs]*5)+'.', groups * 5, 0, 0, 0)
    memo.clear()
    count += c
    print(c)

print(count)
