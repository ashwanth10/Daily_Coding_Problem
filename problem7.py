"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def helper(data, k):
    if k==0 :
        return 1

    s = len(data) - k
    if data[s] == '0':
        return 0

    result = helper(data, k - 1)
    if k>=2 and int(data[s:s+2]) <= 26:
        result += helper(data, k - 2)
    return result

def no_ways(data):
    r = helper(data, len(data))
    print("The no of ways are: {}".format(r))

def main():
    s =raw_input("Enter string: ")
    print("Entered string:" + s)
    s = s.strip()
    no_ways(s)

if __name__ == '__main__' :
    main()