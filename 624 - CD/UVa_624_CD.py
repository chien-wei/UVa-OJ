import sys

input = sys.stdin.readline().strip()

# 0/1 knapsack
while input != '':
    input = input.split()
    capacity = int(input[0])
    num_item = int(input[1])
    item = [int(i) for i in input[2:]]
    dp = [[0 for _ in range(capacity + 1)] for _ in range(num_item + 1)]
    put = [[False for _ in range(capacity + 1)] for _ in range(num_item)]

    for n in range(num_item):
        for c in range(capacity+1):
            if c < item[n]:
                dp[n+1][c] = dp[n][c]
            else:
                if dp[n][c-item[n]] + item[n] > dp[n][c]:
                    dp[n+1][c] = dp[n][c-item[n]] + item[n]
                    put[n][c] = True
                else:
                    dp[n+1][c] = dp[n][c]
    # go back to found which item in knapsack
    res = []
    w = len(put[0])-1
    for i in range(len(put))[::-1]:
        if put[i][w]:
            res.append(item[i])
            w -= item[i]
    res = [str(r) for r in res[::-1]]
    print('{:} sum:{:d}'.format(" ".join(res), dp[num_item][capacity]))
            


    input = sys.stdin.readline().strip()