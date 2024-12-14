file = 'in.txt'

with open(file) as f:
    text = f.read()
    rules_text, ords = text.split('\n\n')

    rules = []
    for line in rules_text.split('\n'):
        rules.append(line.split('|'))

    orderings = []
    for line in ords.split('\n'):
        if line:
            orderings.append(line.split(','))

# Maps after values to before values
from collections import defaultdict

after_map = defaultdict(list)
for rule in rules:
    after_map[rule[1]].append(rule[0])


def is_ordering_correct(ordering):
    # Track visited values that have after values
    # If we encounter a before value then its wrong
    before_values = []
    for value in ordering:
        if value in before_values:
            return False

        if value in after_map:
            before_values += after_map[value]

    return True

# Part 2
from functools import cmp_to_key

def fix_ordering(ordering):
    def custom_sort(a, b):
        if [a, b] in rules:
            return -1
        elif [b, a] in rules:
            return 1
        else:
            return 0

    ordering.sort(key=cmp_to_key(custom_sort))
    return ordering


total = 0
for ordering in orderings:
    if not is_ordering_correct(ordering):
        ord = fix_ordering(ordering)
        idx = len(ord) // 2
        total += int(ord[idx])

print(total)

