with open('in.txt') as f:
    pt = [l for l in f.read().split('\n\n') if l]
    pt = [p.split('\n') for p in pt]
    patterns = []
    i = 0
    for p in pt:
        patterns.append([])
        for row in p:
            patterns[i].append([r for r in row])
        i += 1

def get_reflection(pat, prev_r, prev_c):
    frows = []
    fcols = []
    # Check rows for vertical reflectinons
    for r in range(len(pat)-1):
        if pat[r] == pat[r+1]:
            frows.append(r)
    
    # Check cols for horizontal reflections
    for c in range(len(pat[0])-1):
        if get_col_val(pat, c) == get_col_val(pat, c+1):
            fcols.append(c)
    
    for rl in frows:
        if rl == prev_r:
            continue
        if check_rows(pat, rl):
            return rl, None

    for cl in fcols:
        if cl == prev_c:
            continue
        if check_cols(pat, cl):
            return None, cl
    
    return None, None
    

def get_col_val(pat, col):
    c = ''
    for r in range(len(pat)):
        c += pat[r][col]
    return c

def check_rows(pat, r):
    i = 1
    while (r-i) >= 0 and (r+i+1) < len(pat):
        if pat[r+i+1] != pat[r-i]:
            return False
        i += 1
    return True


def check_cols(pat, col):
    c = col
    i = 1
    while (c-i) >= 0 and c+i+1 < len(pat[0]):
        if get_col_val(pat, c-i) != get_col_val(pat, c+i+1):
            return False
        i +=1
    return True

rows = []
cols = []
for i, pattern in enumerate(patterns):
    prev_r, prev_c = get_reflection(pattern, None, None)
    done = False
    for i in range(0, len(pattern)):
        for j in range(0, len(pattern[0])):
            new_pattern = [p[:] for p in pattern]
            new_pattern[i][j] = '.' if new_pattern[i][j] == '#' else '.'
            row, col = get_reflection(new_pattern, prev_r, prev_c)           
            if col is not None:
                cols.append(col+1)
                done = True
                break
            if row is not None:
                done = True
                rows.append(row+1)
                break
            if done:
                break
        if done:
            break

print(len(rows) + len(cols))
print(sum(cols) + (sum(rows) * 100))
