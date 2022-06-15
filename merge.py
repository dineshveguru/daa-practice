n = int(input("enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i + 1}th element: ")))


def sort(arr):
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    sort(left)
    sort(right)

    merge(left, right, arr)


def merge(arr1, arr2, result):
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            k += 1
            i += 1
        elif arr2[j] <= arr1[i]:
            result[k] = arr2[j]
            k += 1
            j += 1
    while i < len(arr1):
        result[k] = arr1[i]
        k += 1
        i += 1
    while j < len(arr2):
        result[k] = arr2[j]
        k += 1
        j += 1


sort(arr)
print(arr)
