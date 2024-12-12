from collections import defaultdict 

with open('input.txt') as f:
    list_a = []
    list_b = []
    for line in f.readlines():
        a, b = line.split('  ')
        list_a.append(int(a.strip()))
        list_b.append(int(b.strip()))

    def part_1():
    
        list_a.sort()
        list_b.sort()

        # Assuming same length
        total = 0
        for i in range(len(list_a)):
            diff = abs(list_a[i] - list_b[i])
            total += diff

        print(total)

    def part_2():
        
        right_counts = defaultdict(int) 
        for b in list_b:
            right_counts[b] += 1
        
        total = 0
        for a in list_a:
            total += a * right_counts[a]

        print(total)

    part_2()
        
