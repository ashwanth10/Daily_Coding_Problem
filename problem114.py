"""
Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters.
For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""

def main():
    s = raw_input("Enter the string?\n")
    delimiters = []
    index = 0
    prev_item = ''
    for item in s:
        if item == ':' or item =='/':
            delimiters.append([item, index])
            prev_item = item
            index += 1
        else:
            if prev_item == '' or prev_item == '/' or prev_item == ':':
                index += 1
                prev_item = item

    s = s.replace('/', ':')
    s = s.split(':')
    s.reverse()

    while(s[0] == ''):
        s.reverse()
        s.pop()
        s.reverse()
        s.append('')

    for delimiter in delimiters:
        item, index = delimiter
        s.insert(index, item)

    s = ''.join(s)

    print(s)

if __name__ == '__main__':
    main()