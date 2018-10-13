# This dp solution get TLE, should directly count it.
import sys

input = sys.stdin.readline().strip()

while input != '':
    [m, n, t] = [int(i) for i in input.split()]
    c = [-1 for _ in range(t+1)]
    c[0] = 0
    for i in range(1, len(c)):
        for w in [m, n]:
            if i-w >= 0 and c[i-w] != -1:
                c[i] = max(c[i], c[i-w] + 1)

    use_all_time = True
    finishd_time = t
    for i in range(t+1)[::-1]:
        if c[i] != -1:
            print(c[i], end='')
            if i != t:
                use_all_time = False
                finishd_time = i
            break
    if not use_all_time:
        print(' {:d}'.format(t - finishd_time))
    else:
        print()
    input = sys.stdin.readline().strip()