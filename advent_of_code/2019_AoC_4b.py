from datetime import datetime

startTime = datetime.now()

def count_digits(n):
    """Make sure there are at 6 digits in the sequence."""
    return len(str(n)) == 6

def check_doubles(n):
    """Make sure there are double-digits of at least one pair in the sequence."""
    n = list(str(n))
    previous_d = None
    for d in n:
        if previous_d is None:
            previous_d = d
        else:
            if previous_d == d:
                return True
            previous_d = d
    return False

def check_increase(n):
    """Make sure the numbers are all increasing from left to right."""
    return True if int(''.join(str(digit) for digit in sorted(list(str(n))))) == int(n) else False


def solver(start, finish):
    """Counts how many of the numbers in the sequence might be a password."""
    counter = 0

    for n in range(start, finish+1):
        if count_digits(n) and check_doubles(n) and check_increase(n):
            counter += 1
    
    return f"{counter} matches found."

print(solver(168630, 718098)) # the full test

print(f"Runtime: {datetime.now() - startTime}")