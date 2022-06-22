n = int(input("enter number of elements: "))
wt = []
profits = []
for i in range(n):
    wt.append(int(input(f"enter weight for {i}th element: ")))
    profits.append(int(input(f"enter profit for {i}th element: ")))
capacity = int(input("enter the capacity of knapsack: "))


def sol(wt, profits, capacity):
    n = len(wt)
    table = [[0 for i in range(capacity + 1)] for i in range(n + 1)]
    for i in range(len(wt) + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                table[i][j] = max(profits[i - 1] + table[i - 1]
                                  [j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    return table[n][capacity]


print(sol(wt, profits, capacity))
