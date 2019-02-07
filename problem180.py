"""
Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue.
This should be done in-place.
Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.
For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
Hint: Try working backwards from the end state.
"""


class stack():
    def __init__(self):
        self.elements = []
        self.size = 0

    def push(self, item):
        self.elements.append(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            item = -1
        else:
            item = self.elements.pop()
            self.size -= 1
        return item


class queue():
    def __init__(self):
        self.elements = []
        self.size = 0

    def enqueue(self, item):
        self.elements.append(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            item = -1
        else:
            item = self.elements[0]
            self.elements = self.elements[1:]
            self.size -= 1
        return item


def main():
    s = stack()
    q = queue()
    elements = map(int, raw_input('enter elements of stack?\n').split())
    for item in elements:
        s.push(item)

    count = 1
    while(True):
        if count == len(elements):
            break
        while(count != s.size):
            q.enqueue(s.pop())
        while(q.size):
            s.push(q.dequeue())
        count += 1
    print(s.elements)


if __name__ == '__main__':
    main()