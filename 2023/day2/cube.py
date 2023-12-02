
"""
Day 2: Cubes

General idea

1. Iterate each word in the line split by ' '
2. Clean word (remove ;,\n)
3. If word is a color the value is behind it
"""

def get_power(line):
    colors = {'blue': [], 'red': [], 'green': []}
    words = line.split(' ')
    for i, l in enumerate(words):
        lclean = l.replace(';', '').replace(',', '').strip()
        if lclean in colors:
            colors[lclean].append(int(words[i - 1]))
        
    return max(colors['blue']) * max(colors['green']) * max(colors['red'])

games = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        games += get_power(line)
    
print(games)
