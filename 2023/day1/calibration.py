"""
Read the input file

for each line get first and last digit

Determine the sum of all values
"""

def get_first_char(line, digits):
    accumulator = ''
    for ch in line:
        try:
            val = int(ch)
            return val
        except:
            accumulator += ch
            for digit_str in digits:
                if digit_str in accumulator:
                    return digits[digit_str]
            continue

def get_calibration_value(line):
    digits = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    reverse_digits = {label[::-1]: val for label, val in digits.items()}
    first, last = get_first_char(line, digits), get_first_char(line[::-1], reverse_digits)
    return int(f'{first}{last}')

def read_input():
    values = []
    with open('input_1.txt', 'r') as f:
        for line in f.readlines():
            values.append(get_calibration_value(line))

    return values

def main():
   values = read_input()
   print(sum(values))


if __name__ == "__main__":
    main()
