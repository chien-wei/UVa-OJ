# UVa 674 Coin Change
# Problem description: https://uva.onlinejudge.org/external/6/674.pdf
# Author: Chien-Wei Sun

import sys

ways_to_change = [0 for _ in range(7490)]
ways_to_change[0] = 1
coin_values = [1, 5, 10, 25, 50]
for v in coin_values:
    for i in range(v, len(ways_to_change)):
        ways_to_change[i] += ways_to_change[i-v]

input = sys.stdin.readline().strip()
while input != '':
    print(ways_to_change[int(input)])
    input = sys.stdin.readline().strip()