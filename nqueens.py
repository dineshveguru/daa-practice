n = int(input())
col = set()
posdiag = set()
negdiag = set()
board = [["." for i in range(n)] for i in range(n)]


def print_arr(arr):
    for i in arr:
        for j in i:
            print(j, end="    ")
        print("\n")


def backtrack(r):
    i = 0
    if r == n:
        print(f"{i}st solution")
        i += 1
        print_arr(board)
        return
    for c in range(n):
        if c in col or (r + c) in posdiag or (r - c) in negdiag:
            continue
        col.add(c)
        posdiag.add(r + c)
        negdiag.add(r - c)
        board[r][c] = "Q"
        backtrack(r + 1)
        col.remove(c)
        posdiag.remove(r + c)
        negdiag.remove(r - c)
        board[r][c] = "."


backtrack(0)
