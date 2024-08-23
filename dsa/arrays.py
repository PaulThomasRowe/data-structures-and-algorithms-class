# Static Arrays
class StaticArray:
    def insertEnd(arr, n, length, capacity):
        if length < capacity:
            arr[length] = n

    def removeEnd(arr, length):
        if length > 0:
            arr[length - 1] = 0

    def insertMiddle(arr, i, n, length):
        for index in range(length - 1, i - 1, -1):
            arr[index + 1] = arr[index]
        arr[i] = n

    def removeMiddle(arr, i, length):
        for index in range(i + 1, length):
            arr[index - 1] = arr[index]

    def printArr(arr, capacity):
        for i in range(capacity):
            print(arr[i])


# Dynamic Arrays
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2

    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def popback(self):
        if self.length > 0:
            self.length -= 1

    def get(self, i):
        if i < self.length:
            return self.arr[i]

    def insert(self, i, n):
        if i < self.length:
            self.arr[i] = n
            return

    def print(self):
        for i in range(self.length):
            print(self.arr[i])
        print()


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()


# Source: Neetcode