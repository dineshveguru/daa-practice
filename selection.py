n = int(input("enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i + 1}th element: ")))


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


def selection(arr):
    for i in range(n):
        min_element_index = i
        for j in range(i, n):
            if arr[j] < arr[min_element_index]:
                min_element_index = j
        swap(i, min_element_index, arr)


selection(arr)
print(arr)
