"""
Boy that was rough
"""

def get_seeds_p1(line):
    return [int(n) for n in line.replace('seeds: ', '').split(' ')]

def get_seeds_p2(line):
    values = get_seeds_p1(line)
    ranges = []
    seeds = []
    for i in range(0, len(values)-1, 2):
        ranges.append(values[i + 1])
        seeds.append(values[i])
    
    return [(seeds[i], seeds[i] + ranges[i]) for i in range(len(seeds))]

almanac = {}
with open('input.txt') as f:
    text = [line for line in f.read().split('\n') if line != '']
    i = 0
    while i < len(text):
        if 'map' in text[i]:
            key = text[i].replace(' map:', '')
            almanac[key] = []
            i += 1
            while i < len(text):
                if 'map' in text[i]:
                    i -= 1 # yuck
                    break
                [dest_start, source_start, range_len] = [int(n) for n in text[i].split(' ')]
                almanac[key].append((dest_start, source_start, range_len))
                i += 1
        i += 1

    # (dest_start, source_start, range_len)
    # mapping: dest => dest_start + (source - source_start) if source in range
    # 52, 50, 48
    # 53 => 55

    # Part 1
    # seeds = get_seeds_p1(text[0])
        
    # sources = []
    # for seed in seeds:
    #     print('SEED: ', seed)
    #     source = seed
    #     for key, mappings in almanac.items():
    #         for mapping in mappings:
    #             (dest_start, source_start, range_len) = mapping
    #             if source in range(source_start, source_start + range_len):
    #                 source = dest_start + (source - source_start)
    #                 break
    #     sources.append(source)

    # print(min(sources))

    # Part 2 - Intervals and intervals and more intervals
    from itertools import count
    seeds = get_seeds_p2(text[0])
    def is_valid_seed(seeds, seed):
        for min_s, max_s in seeds:
            if seed >= min_s and seed < max_s:
                return True
                
        return False

    # Count up (locations) and map - if result is a valid seed then return the starting location
    for seed in count(1):
        source = seed
        for key, mappings in reversed(almanac.items()):
            for mapping in mappings:
                (dest_start, source_start, range_len) = mapping
                # Reverse process from before
                if source in range(dest_start, dest_start + range_len):
                    source = source_start + (source - dest_start)
                    break

        if is_valid_seed(seeds, source):
            print(seed)
            exit()



