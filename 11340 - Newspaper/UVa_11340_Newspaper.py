import sys
import collections


input = sys.stdin.readline().strip()
n = int(input)
for i in range(n):
    ans = 0
    input = sys.stdin.readline().strip()
    num_char = int(input)
    prices = collections.defaultdict(int)
    for j in range(num_char):
        input = sys.stdin.readline().strip()
        tmp = input.split(' ')
        prices[tmp[0]] = int(tmp[1])
    input = sys.stdin.readline().strip()
    num_line = int(input)
    for k in range(num_line):
        input = sys.stdin.readline().strip()

        for c in input:
            ans += prices[c]
    print('%.2f$'%(ans/100))

    
