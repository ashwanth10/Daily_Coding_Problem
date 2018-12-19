"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].
Lesson Learnt: To remove the first element, you can use list[1:] instead of reverse(), pop() and again reverse()
"""

def main():
    list_of_elements = map(int, raw_input('Enter list of elements?\n').split())
    k = int(raw_input("Enter K?\n"))

    answer_list = []
    index = 0

    while(index < len(list_of_elements)):
        list_sum = sum(answer_list)
        if list_sum < k:
            answer_list.append(list_of_elements[index])
            index += 1
        elif list_sum == k:
            break
        else:
            answer_list = answer_list[1:]

    if(sum(answer_list) == k):
        print(answer_list)
    else:
        print("No Found!")


if __name__ == '__main__':
    main()