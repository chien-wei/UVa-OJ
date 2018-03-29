import sys

input = sys.stdin.readline().strip()

while input != '':
    N, D = map(int, input.split(' '))
    boxes = []
    for i in range(N):
        input = sys.stdin.readline().strip()
        boxes.append(sorted(map(int, input.split(' '))) + [i+1]) # the last index means its origin order (1-based)
    boxes = sorted(boxes)

    max_len = [1 for _ in range(N)]
    pre = [-1 for _ in range(N)]

    for i in range(1, N):
        for j in range(i-1, -1, -1):
            j_smaller = True
            for k in range(D):
                if boxes[j][k] >= boxes[i][k]:
                    j_smaller = False
                    break
            if j_smaller and max_len[j] + 1 > max_len[i]:
                max_len[i] = max_len[j] + 1 # max
                pre[i] = j # index of pre
    
    result = []
    end_index = max_len.index(max(max_len))
    print(max(max_len))
    while end_index >= 0: # we init pre as -1
        result.append(boxes[end_index][D])
        end_index = pre[end_index]
    print(*result[::-1])

    input = sys.stdin.readline().strip()