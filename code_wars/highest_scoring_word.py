# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def high(x):
    
    max_score = 0

    for word in x.split(' '):

        score = 0

        for char in word:
            score += ord(char) - 96
        
        if score > max_score:
            highest = word
            max_score = score

    return highest


# "test"-cases
print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))