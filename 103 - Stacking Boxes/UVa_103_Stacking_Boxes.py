# solution using LIS
import sys

class Box:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.dimention = len(size)
    
    def __gt__(self, other):
        for i in range(self.dimention):
            if self.size[i] < other.size[i]:
                return False
        return True
    def __repr__(self):
        return str(self.id)


input = sys.stdin.readline().strip()

while input != '':
    N, D = map(int, input.split(' '))
    boxes = []
    for i in range(N):
        input = sys.stdin.readline().strip()
        boxes.append(Box(i+1, sorted(map(int, input.split(' ')))))
    boxes = sorted(boxes)

    max_len = [1 for _ in range(N)]
    parent = [-1 for _ in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            if boxes[i] < boxes[j]:
                if max_len[i] + 1 > max_len[j]:
                    max_len[j] = max_len[i] + 1
                    parent[j] = i

    # print result
    result = []
    length = max(max_len)
    end_index = max_len.index(length)
    print(length)
    while end_index >= 0: # we init parent as -1
        result.append(boxes[end_index].id)
        end_index = parent[end_index]
    print(*result[::-1])

    input = sys.stdin.readline().strip()


# solution of Longest Path in a Directed Acyclic Graph
# ref: https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
# If shortest: Use Floyd-Warshall: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
# Author: Kenway Sun
# Date: 2018-09-22