n = int(input("enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i + 1}th element: ")))


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def partition(arr, start, end):
    b = start - 1
    pivot = arr[end]
    for i in range(start, end + 1):
        if arr[i] <= pivot:
            b += 1
            swap(arr, i, b)
    return b


def sort(arr, start, end):
    if start >= end:
        return
    boundary = partition(arr, start, end)
    sort(arr, start, boundary - 1)
    sort(arr, boundary + 1, end)


sort(arr, 0, len(arr) - 1)
print(arr)
