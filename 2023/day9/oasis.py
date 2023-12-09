
def get_differences(history):
    diffs = []
    for i in range(len(history) - 1):
        diffs.append(history[i+1]-history[i])
    
    return diffs


def extrapolate(differences: list[list[int]]):
    """
    Loop diff lists in reverse
    Keep adding the last value in the list to the previous last

    Going upwards we are finding the X so that X - Y = Z
    X = New last item in the line we are on
    Y = Current last item in the line we are on
    Z = last value for previous line

    X = Z + Y
    """

    next_val = 0
    for diffs in differences[::-1]:
        next_val = diffs[-1] + next_val
    return next_val

def extrapolate_part2(differences: list[list[int]]):
    """
    Since its at the beginning now we do the last item minus previous last
    X - Y = Z; Now we are finding Y where X is the first item in the list
    Y = X - Z
    """
    
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

        predictions.append(extrapolate_part2(differences))

    print(sum(predictions))
