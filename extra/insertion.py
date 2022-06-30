n = int(input("enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i + 1}th element: ")))

for i in range(len(arr)):
    current = arr[i]
    j = i - 1
    while (j >= 0 and arr[j] > current):
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = current

print(arr)
