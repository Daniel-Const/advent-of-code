
def get_differences(history):
    diffs = []
    for i in range(len(history) - 1):
        diffs.append(history[i+1]-history[i])
    
    return diffs


def extrapolate(differences):
    next_val = 0
    for diffs in differences[::-1]:
        next_val = diffs[0] - next_val
    return next_val

with open('in.txt') as f:
    histories = f.read().split('\n')
    histories = [[int(h) for h in hist.split(' ') if h] for hist in histories if hist]
    predictions = []
    for history in histories:
        differences = [history]
        diff = history
        while True:
            differences.append(diff := get_differences(diff))
            if all(d == 0 for d in diff):
                break

        predictions.append(extrapolate(differences))

    print(sum(predictions))
