"""
Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters.
For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""

def main():
    s = raw_input("Enter the string?\n")
    delimiters = []
    temp_stor = ''
    for item in s:
        if item == ':' or item =='/':
            delimiters.append(item)

    s = s.replace('/', ':')
    s = s.split(':')

    answer = ''
    while not answer:
        answer = s.pop()

    delimiters.reverse()
    len_of_string = len(s)
    i = len_of_string - 1
    while(delimiters and i >= 0):
        temp = i
        while(temp > 0 and s[temp-1] == ''):
            temp_stor += delimiters.pop()
            temp -= 1
        answer += ((temp_stor + delimiters.pop()) if temp_stor else delimiters.pop()) + s.pop()
        temp_stor = ''
        i -= 1

    while(i>=0):
        answer += s[i]
        i -= 1
    while delimiters:
        answer += delimiters.pop()

    print(answer)



if __name__ == '__main__':
    main()