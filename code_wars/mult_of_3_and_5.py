# https://www.codewars.com/kata/multiples-of-3-or-5/train/python

def solution(number):
  
    i = 1
    multiple = 0
    array_of_multiples = []
    sum_of_multiples = int()

    while multiple < number:
        multiple = i * 3
        if multiple >= number:
            break
        array_of_multiples.append(multiple)
        i += 1

    i = 1
    multiple = 0

    while multiple < number:
        multiple = i * 5
        if multiple >= number:
            break
        array_of_multiples.append(multiple)
        i += 1

    for val in array_of_multiples:
        sum_of_multiples += val

    return sum_of_multiples

# "test"-cases
# print(solution(10))  # should equal 23
print(solution(93))  # should equal 23
# print(solution(10533))  # should equal 23
