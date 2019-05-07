# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python

def count_sheeps(arrayOfSheeps):

    sheep_count = 0
  
    for sheep in arrayOfSheeps:
        if sheep is True:
            sheep_count += 1
          
    return sheep_count