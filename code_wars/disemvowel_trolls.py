# https://www.codewars.com/kata/disemvowel-trolls/train/python

def disemvowel(string):

    trolledified_stringything = str()

    for char in string:
        if char not in "aeiouAEIOU":
            trolledified_stringything += char

    return trolledified_stringything

# "test"-case
print(disemvowel("This website is for losers LOL!"))