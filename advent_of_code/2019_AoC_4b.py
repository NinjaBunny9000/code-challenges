# https://adventofcode.com/2019/day/4

from datetime import datetime

startTime = datetime.now()

def count_digits(n):
    """Make sure there are at 6 digits in the sequence."""
    return len(str(n)) == 6

def check_doubles(n):
    """Make sure there are double-digits of at least one pair in the sequence, but that
    they're not part of a larger group."""
    n = list(str(n))
    repeat_counter = 1
    prev_d = None
    pairs = 0 
    for i, d in enumerate(n):    
        # handle the first digit
        if prev_d is None:
            prev_d = d
        # count all repeating digits
        elif prev_d == d:
            repeat_counter += 1
            if i == 5 and repeat_counter == 2:
                pairs += 1     
        # keep count of pairs of 2
        else:
            if repeat_counter == 2:
                pairs += 1
            repeat_counter = 1
        prev_d = d # reset for next loop
    return pairs >= 1

def check_increase(n):
    """Make sure the numbers are all increasing from left to right."""
    return True if int(''.join(str(digit) for digit in sorted(list(str(n))))) == int(n) else False

def password_finder(start, finish):
    """Counts how many of the numbers in the sequence might be a password."""
    counter = 0
    for n in range(start, finish+1):
        if count_digits(n) and check_doubles(n) and check_increase(n):
            counter += 1
    return f"{counter} matches found."

print(password_finder(168630, 718098))  # test the full range

print(f"Run time: {datetime.now() - startTime}")  # track how long it took to run