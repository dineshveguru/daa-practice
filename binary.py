n = int(input("enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i + 1}th element: ")))
element = int(input("enter the element to be searched: "))


def search(arr, element, start, end):
    if start > end:
        return -1
    mid_index = (start + end) // 2
    if arr[mid_index] == element:
        return mid_index
    elif arr[mid_index] > element:
        return search(arr, element, start, mid_index - 1)
    elif arr[mid_index] < element:
        return search(arr, element, mid_index + 1, end)


print(search(arr, element, 0, n - 1))
