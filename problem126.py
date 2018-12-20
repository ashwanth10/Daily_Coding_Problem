"""
Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
Try solving this without creating a copy of the list.
How many swap or move operations do you need?
"""

def main():
    intial_list = map(int, raw_input("Enter first list?\n").split())
    final_list = map(int, raw_input("Enter final list?\n").split())

    k = 0
    while(k < len(intial_list)):
        if intial_list == final_list:
            print(k)
            break
        else:
            k += 1
            intial_list = intial_list[1:] + intial_list[:1]

if __name__ == '__main__':
    main()