backtrack(r + 1)
            col.remove(c)
            posdiag.remove(r + c)
            negdiag.remove(r - c)
            board[r][c] = "."