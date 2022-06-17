n = int(input("enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i + 1}th element: ")))
element = int(input("enter the element to be searched: "))


def search(arr, element):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            end = mid - 1
        elif arr[mid] < element:
            start = mid + 1
    else:
        return -1


print(search(arr, element))
