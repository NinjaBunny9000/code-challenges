# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python

def title_case(title, minor_words=''):

    title = title.lower().title().split(' ')  # title case everything
    title_cased = [title[0]]  # keep the first char capitalized

    for word in title[1:]:

        # lower-case minor words
        if word.lower() in minor_words.lower().split(' '):
            title_cased.append(word.lower())
        
        # leave the rest the same
        else:
            title_cased.append(word)

    return ' '.join(title_cased)


# "test"-cases
print(title_case(''))
print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox'))