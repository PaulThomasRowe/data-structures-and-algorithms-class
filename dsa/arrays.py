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

# Source: Neetcode