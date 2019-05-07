# https://www.codewars.com/kata/who-likes-it/train/python

def likes(names):
    
    likers = len(names)

    if likers == 0:
        return "no one likes this"

    elif likers == 1:
        return f"{names[0]} likes this"

    elif likers == 2:
        return f"{names[0]} and {names[1]} like this"
    
    elif likers == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    elif likers > 3:
        return f"{names[0]}, {names[1]} and {likers - 2} others like this"


# "test" cases
print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))