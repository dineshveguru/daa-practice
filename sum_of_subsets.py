n = int(input("enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"enter {i + 1}th element: ")))
target_sum = int(input("enter the target sum: "))


def sos(arr, target_sum, l1, i, sum_now):
    if target_sum < sum_now:
        return
    if target_sum == sum_now:
        print(l1)
        return
    if i == len(arr):
        return

    l2 = l1.copy()
    l1.append(arr[i])
    sos(arr, target_sum, l1, i + 1, sum(l1))
    sos(arr, target_sum, l2, i + 1, sum(l2))


sos(arr, target_sum, [], 0, 0)
