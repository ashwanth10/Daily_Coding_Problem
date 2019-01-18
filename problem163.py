"""
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.
The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.
For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
You can assume the given expression is always valid.
"""

def main():
    notation = raw_input('enter notation?\n').split()
    num_stack = []

    for item in notation:
        if item not in ['+', '-', '/', '*']:
            num_stack.append(item)
        else:
            num2 = int(num_stack.pop())
            num1 = int(num_stack.pop())
            if item == '+':
                result = num1 + num2
            elif item == '-':
                result = num1 - num2
            elif item == '*':
                result = num1 * num2
            elif item == '/':
                result = num1 / num2
            else:
                print('invalid operator {}'.format(item))
            num_stack.append(result)

    print(num_stack[0])

if __name__ == '__main__':
    main()
