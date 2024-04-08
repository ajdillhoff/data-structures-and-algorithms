def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0 for _ in range(n+1)] for _ in range(m+1)]
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "↖"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "←"
    return c, b

def print_lcs(b, X, i, j, result):
    if i == 0 or j == 0:
        return
    if b[i][j] == "↖":      # characters are the same, print
        print_lcs(b, X, i-1, j-1, result)
        result.append(X[i-1])
    elif b[i][j] == "↑":    # move up the table
        print_lcs(b, X, i-1, j, result)
    else:                   # move left in the table
        print_lcs(b, X, i, j-1, result)


if __name__ == "__main__":
    X = "amputation"
    Y = "spanking"
    c, b = lcs_length(X, Y)
    result = []
    print_lcs(b, X, len(X), len(Y), result)
    result = "".join(result)
    print(result)