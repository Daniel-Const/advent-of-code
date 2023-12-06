import math

def parse_part_2(text):
    times, distances = text.split('\n')
    filt = lambda line: [x.strip() for x in line.split(' ') if x != '']
    times, distances = filt(times.split('Time: ')[1]), filt(distances.split('Distance: ')[1])
    time = int(''.join([t for t in times]))
    distance = int(''.join([d for d in distances]))
    return time, distance 

def get_distance(speed, time):
    return speed * time

def part_1(text):
    times, distances = text.split('\n')
    filt = lambda line: [int(x.strip()) for x in line.split(' ') if x != '']
    times, distances = filt(times.split('Time: ')[1]), filt(distances.split('Distance: ')[1])
    total_counts = []
    for i, t in enumerate(times):
        counts = 0
        for button_press in range(0, 2000):
            actual_time = t - button_press
            if actual_time < 0:
                break
            distance = get_distance(button_press, actual_time)
            if distance > distances[i]:
                counts += 1
        total_counts.append(counts)
    
    val = 1
    for c in total_counts:
        val *= c
    
    return val

def part_2(text):
    time, distance = parse_part_2(text)
    counts = 0
    for button_press in range(0, distance):
        t = time - button_press
        if t < 0:
            break
        d = get_distance(button_press, t)
        if d > distance:
            counts += 1

    return counts

def part_2_better(text):
    """
    We can write an expression for the distance with respect to the button presses:

    Speed = s, time = t, available_time = t'
    s = b
    t = t' - b
    d = (t' - b) * b

    This gives us a parabola.
    - b^2 + t'*b - d = 0

    We can solve for b using the quadratic formula and get all possible values of b for any given
    distance d (t' is a constant)

    Then, plug in the record distance (record_d) and get two values
    b1, b2

    This represents the b values where the parabola intersects the line d = record_d
    
    All the button values in between this range will be distances greater than the record
    so their difference gives us the solution (the parabola is concave down)
    """

    time, distance = parse_part_2(text)
    b1 = ((-time) + math.sqrt((time**2 - 4 * distance))) / -2
    b2 = ((-time) - math.sqrt((time**2 - 4 * distance))) / -2
    return(int(b2 - b1))


with open('in.txt') as f:
    text = f.read()
    print(part_1(text))
    # print(part_2(text))
    print(part_2_better(text))


