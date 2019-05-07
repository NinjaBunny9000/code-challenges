# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    
    # pass all empty strings
    if len(string) is 0:
        return True
    
    # if it's not alpha or has spaces - fail
    elif not string.lower().isalpha() or string.lower().isspace():
        return False
    
    mask = ""

    for char in string.lower():
        # if the char is already in the string, it's not an isogram
        if char in mask:
            return False
        else:
            mask += char
            
    # if it made it this far, it's totes isogram
    return True