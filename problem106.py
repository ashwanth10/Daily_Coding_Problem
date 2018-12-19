"""

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.
"""

def main():
    given_list = map(int, raw_input("Enter the list?\n").split())

    value = given_list[0]
    index = 0

    while(value > 0 and not (index >= (len(given_list) - 1))):
        index += value
        value = given_list[index]

    print(index >= (len(given_list) - 1))


if __name__ == '__main__':
    main()