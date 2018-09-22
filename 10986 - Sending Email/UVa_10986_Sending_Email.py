# UVa 10986 Sending Email
# Problem description: https://uva.onlinejudge.org/external/109/10986.pdf
# Author: Chien-Wei Sun

import sys
from queue import PriorityQueue

class Delay(object):
    def __init__(self, server, time):
        self.server = server
        self.time = time
        return
    # python3 has no __cmp__, it can uses:
    def __eq__(self, other):
        return self.time == other.time
    def __ne__(self, other):
        return self.time != other.time
    def __gt__(self, other):
        return self.time > other.time
    def __lt__(self, other):
        return self.time < other.time
    def __ge__(self, other):
        return self.time >= other.time
    def __le__(self, other):
        return self.time <= other.time


input = sys.stdin.readline().strip()
N = int(input)

for case in range(N):
    input = sys.stdin.readline().strip()
    [n, m, S, T] = [int(v) for v in input.split()]

    # Set-up. Use dict as a sparse matrix instead of 2d list to prevent TLE in UVaOj.
    weight = {}
    for i in range(n):
        weight[i] = {}
    for _ in range(m):
        input = sys.stdin.readline().strip()
        [s1, s2, value] = [int(v) for v in input.split()]
        weight[s1][s2] = value
        weight[s2][s1] = value 

    # Dijkstra's algorithm
    d = {S: 0}
    pq = PriorityQueue()
    pq.put(Delay(S, 0))
    while not pq.empty():
        delay_obj = pq.get()
        a = delay_obj.server

        for b in weight[a]:
            b_alt_delay = d[a] + weight[a][b]
            # Two ways to prevent negative cycle: 1. use a visited list. 2. set a threshold.
            # I used 2 here.
            if b_alt_delay < -100000:
                raise Exception("Negative cycle detected.")
            if b_alt_delay < d.get(b, float('inf')):
                d[b] = b_alt_delay
                pq.put(Delay(b, b_alt_delay))

    # output
    if T in d:
        print('Case #{:d}: {:d}'.format(case+1, d[T]))
    else:
        print('Case #{:d}: unreachable'.format(case+1))


