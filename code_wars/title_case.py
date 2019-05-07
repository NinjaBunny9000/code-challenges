# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python

def title_case(title, minor_words=''):
    
    if title is '':  # handle empty strings
        return title

    title_cased = []

    for word in title.lower().split(' '):
        
        # don't change minor words
        if word in minor_words.lower().split(' '): 
            title_cased.append(word)

        # switch others to title case
        else: 
            title_cased.append(word.title())

    title_cased.insert(0, title_cased[0].title())  # capitalize the first letter
    title_cased.pop(1)  # pop remove the double entry
    
    return ' '.join(title_cased)

# "test"-cases
print(title_case(''))
print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox'))
