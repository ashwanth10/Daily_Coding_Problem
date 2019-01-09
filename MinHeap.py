"""
Implementation of a Min-Heap.
"""

class MinHeap():

    def __init__(self, size):
        self._elements = [0] * size
        self._size = 0

    def getLeftChildIndex(self, elementIndex):
        return 2 * elementIndex + 1

    def getRightChildIndex(self, elementIndex):
        return 2 * elementIndex + 2

    def getParentIndex(self, elementIndex):
        return (elementIndex - 1) / 2

    def hasLeftChild(self, elementIndex):
        return self.getLeftChildIndex(elementIndex) < self._size

    def hasRightChild(self, elementIndex):
        return self.getRightChildIndex(elementIndex) < self._size

    def isRoot(self, elementIndex):
        return elementIndex == 0

    def getLeftChild(self, elementIndex):
        return self._elements[self.getLeftChildIndex(elementIndex)]

    def getRightChild(self, elementIndex):
        return self._elements[self.getRightChildIndex(elementIndex)]

    def getParent(self, elementIndex):
        return self._elements[self.getParentIndex(elementIndex)]

    def swap(self, firstIndex, secondIndex):
        temp = self._elements[firstIndex]
        self._elements[firstIndex] = self._elements[secondIndex]
        self._elements[secondIndex] = temp

    def isEmpty(self):
        return self._size == 0

    def peek(self):
        if self._size == 0:
            raise IndexError
        return self._elements[0]

    def pop(self):
        if self._size == 0:
            raise IndexError

        result = self._elements[0]
        self._elements[0] = self._elements[self._size - 1]
        self._size -= 1

        self.heapifyDown()
        return result

    def add(self, element):
        if self._size == len(self._elements):
            raise IndexError

        self._elements[self._size] = element
        self._size += 1

        self.heapifyUp()

    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallerIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.getRightChild(index) < self.getLeftChild(index)):
                smallerIndex = self.getRightChildIndex(index)

            if(self._elements[smallerIndex] > self._elements[index]):
                break

            self.swap(smallerIndex, index)
            index = smallerIndex

    def heapifyUp(self):
        index = self._size - 1
        while(not self.isRoot(index) and self._elements[index] < self.getParent(index)):
            parentIndex = self.getParentIndex(index)
            self.swap(index, parentIndex)
            index = parentIndex

    def displayHeap(self):
        print(str(self._elements))

def main():
    size = int(raw_input("size of heap?\n"))
    heap = MinHeap(size)

    while True:
        choice = int(raw_input("1. add element\t2. pop element\t3. peek element\t4. display heap\t5. exit\n"))
        if choice == 1:
            element = int(raw_input("enter element?\n"))
            heap.add(element)
        elif choice == 2:
            print('Removed {}'.format(heap.pop()))
        elif choice == 3:
            print('Top element is {}'.format(heap.peek()))
        elif choice == 4:
            heap.displayHeap()
        elif choice == 5:
            break
        else:
            continue


if __name__ == '__main__':
    main()
