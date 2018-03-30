import sys

input = sys.stdin.readline().strip()

while input != '':
    
    N = int(input)
    input = sys.stdin.readline().strip()
    order_of_event = map(int, input.split(' '))

    event_in_order = [0 for _ in range(N)]
    for event, order in enumerate(order_of_event):
        event_in_order[order-1] = event+1

    correct_ans = {}
    for index, event in enumerate(event_in_order):
        correct_ans[event] = index

    input = sys.stdin.readline().strip()
    while ' ' in input:
        ans_order = map(int, input.split(' '))
        ans_event_in_order = [0 for _ in range(N)]
        for event, order in enumerate(ans_order):
            ans_event_in_order[order-1] = event+1
        ans = []
        for o in ans_event_in_order:
            ans.append(correct_ans[o])
        # then we only need to do lis with 0 to N
        lis = [1 for _ in range(N)]
        for i in range(1, N):
            for j in range(i-1, -1, -1):
                if ans[j] < ans[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
        print(max(lis))


        input = sys.stdin.readline().strip()