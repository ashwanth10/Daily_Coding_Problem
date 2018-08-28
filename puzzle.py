
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