<<<<<<< HEAD
=======

>>>>>>> 6d37603f69024049529cb50ad928da12a5fcd9df
n = int(input("enter number of elements: "))
weights = []
profits = []
for i in range(n):
    weights.append(int(input(f"enter weight for item {i + 1}: ")))
    profits.append(int(input(f"enter profit for item {i + 1}: ")))
knapsack = int(input("enter the weight of knapsack: "))
ratio = list(map(lambda x, y: x / y, profits, weights))
present_weight = 0
present_profit = 0
while present_weight < knapsack:
    max_profit = max(ratio)
    max_profit_index = ratio.index(max_profit)
    if present_weight + weights[max_profit_index] > knapsack:
        add_ratio = (knapsack - present_weight) / weights[max_profit_index]
        present_weight += weights[max_profit_index] * add_ratio
        present_profit += profits[max_profit_index] * add_ratio
    else:
        present_profit += profits[max_profit_index]
        present_weight += weights[max_profit_index]
    ratio.remove(max_profit)
    weights.remove(weights[max_profit_index])
    profits.remove(profits[max_profit_index])

print(present_profit)
print(present_weight)
