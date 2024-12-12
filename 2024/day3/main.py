import re

with open("in.txt") as f:
    instructions = f.read()

def get_next_mul_value(instructions):
    match = re.search(r"mul\([0-9]*,[0-9]*\)", instructions)
    if not match:
        return None, None

    start, end = match.span()
    values = match.group().replace('mul(', '').replace(')', '')
    a, b = values.split(',')
    return end, int(a.strip()) * int(b.strip())

def match_next(instructions, target):
    match = re.search(target, instructions)
    if not match:
        return None
    start, end = match.span()
    return end


"""
- Keep track of the current mul() match position (with offsets)
- Search for the first do / don't before the matched mul
- If a do is first, then add  the value
- If a don't is first, then don't add the value
- Since we are reversing the string we are matching on )(t'nod and )(od which are don't() and do() reversed
"""
total = 0
mul_instructions = instructions
offset = 0
while True:
    mul_pos, value = get_next_mul_value(mul_instructions)
    if mul_pos is None:
        break

    offset = offset+mul_pos
    reverse_check = instructions[:offset]
    do_pos = match_next(reverse_check[::-1], r"\)\(od")
    dont_pos = match_next(reverse_check[::-1], r"\)\(t'nod")
    if dont_pos is None:
        total += value
    elif do_pos is not None and (do_pos - dont_pos < 0):
        total += value

    # Get substring from current mul so re.search grabs the next mul()
    mul_instructions = instructions[offset:]

print(total)
