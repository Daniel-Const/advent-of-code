def is_symbol(ch):
    return ch != '.' and not ch.isdigit() and ch != '\n'
    
schematic = []
total = 0
with open('input.txt', 'r') as f:
    for l in f.readlines():
        schematic.append([ch for ch in l])

# Collect all the part numbers
part_numbers = []
for y in range(len(schematic)):
    x = 0
    while x  < len(schematic[y]):
        if schematic[y][x].isdigit():
            add_value = False
            itX = x
            number = ''
            # Try 8 directions around the char - check for symbol
            while schematic[y][itX].isdigit():
                for checkX, checkY in [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
                    try:
                        if is_symbol(schematic[y + checkY][itX + checkX]):
                            add_value = True 
                            break
                    except:
                        pass
                # Collect the digit chars
                number += schematic[y][itX]
                itX += 1

            val = int(number)
            if add_value:
                part_numbers.append((y, x, itX, val))

            x = itX

        x += 1

for y in range(len(schematic)):
    x = 0
    while x  < len(schematic[y]):
        if schematic[y][x] == '*':
            gears = []
            duplicates = []
            for checkX, checkY in [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
                try:
                   # Dirty - loop all part_numbers - if x and y ranges match then its adjacent to the number
                   for foundY, foundX, foundEndX, val in part_numbers:
                       if y + checkY == foundY and x + checkX in range(foundX, foundEndX):
                            if f'{foundY}{foundX}{val}' not in duplicates:
                                gears.append(val)
                                duplicates.append(f'{foundY}{foundX}{val}')
                            break
                except:
                    pass
            
            if len(gears) == 2:
                total += gears[0] * gears[1]

        x += 1

print(total)
