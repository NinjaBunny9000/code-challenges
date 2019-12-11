# https://www.codewars.com/kata/strip-comments/train/python

def solution(string,markers):
    split_into_lines = string.split("\n")
    working_line = ''
    comments_removed = []
    for line in split_into_lines:
        for char in line:
            if char not in markers:
                working_line += char
            else:
                break
        try:
            if working_line[-1] == " ":
                comments_removed.append(working_line[:-1])
            else:
                comments_removed.append(working_line)
            working_line = ''
        except IndexError:
            print(string)
    
    comments_removed = '\n'.join(comments_removed)

    return comments_removed

    # rejoin again


# "apples, pears\ngrapes\nbananas"
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])) 
# print(strip_comments("a #b\nc\nd $e f g", ["#", "$"]))  # "a\nc\nd"