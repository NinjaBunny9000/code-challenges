# https://www.codewars.com/kata/strip-comments/train/python

def solution(string,markers):

    # TODO preserve \n as empty string (in cases of \n\n)
    # TODO preserve leading \n
    
    # handle string='\n'
    if string is '\n':
        return string

    # split_into_lines = string.split("\n")
    split_into_lines = string.splitlines(True)

    print(f"string={repr(string)}")
    # print(f"markers={repr(markers)}")
    print(f"split={repr(split_into_lines)}")

    working_line = ''
    comments_removed = []
    # iterate through each line in the list/string
    for line in split_into_lines:
        # iterate through each character in each line
        for char in line:
            # if the character isn't a marker, add it to the "ok"/working_line string
            if char not in markers:
                working_line += char
            #otherwise, exit the loop and go to the next line
            else:
                break
        try:
            # take out any spaces at the ends of the line, if there are any
            if working_line[-1] == " ":
                comments_removed.append(working_line[:-1])
            # add the clean line to the list
            else:
                # print(f"{(working_line)=}")
                # print(f"{(working_line[-1:])=}")
                comments_removed.append(working_line)
                if working_line[-1] == '\n':
                    # print(f"last char is \\n! {working_line=}")
                    pass
                else:
                    comments_removed.append("\n")  # add a return at the end of the line
            working_line = ''
        
        # DEBUG if the string is empty, print it out and make sure there wasn't a mistake
        except IndexError:
            # print(f"IndexError: {line=}")
            pass
    
    # rejoin again
    comments_removed = ''.join(comments_removed)
    print(f"joined={repr(comments_removed)}")
    return repr(comments_removed)



# "apples, pears\ngrapes\nbananas"
# print(solution('apples, pears # and bananas\ngrapes\navocado @apples', ["@"])) 
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])) 
# print(strip_comments("a #b\nc\nd $e f g", ["#", "$"]))  # "a\nc\nd"

"""






"""