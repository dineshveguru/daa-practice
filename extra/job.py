jobs = ([['a', 100, 2], ['c', 27, 2], ['d', 25, 1], [
    'b', 19, 1], ['e', 15, 3]])
n_jobs = 0
for i in jobs:
    if i[2] > n_jobs:
        n_jobs = i[2]
selected = [False for i in range(n_jobs)]
profit = ['0' for i in range(n_jobs)]
for i in range(len(jobs)):
    current = jobs[i]
    for j in range(current[2] - 1, -1, -1):
        if not selected[j]:
            profit[j] = current[1]
            selected[j] = True
            break

for i in profit:
    for j in jobs:
        if i == j[1]:
            print(j[0], end=' ')
            break
