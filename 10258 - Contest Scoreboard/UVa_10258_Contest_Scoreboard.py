import sys

input = sys.stdin.readline().strip()

N = int(input)

input = sys.stdin.readline().strip() # blank

for count in range(N):
    input = sys.stdin.readline().strip()
    info = {}
    while input != '':
        name, problem, time, stat = input.split(' ')
        time = int(time)
        name = int(name)
        problem = int(problem)

        if stat == 'C':
            if name not in info:
                info[name] = [1, time, name, {problem:-1}] # problem, time, name, panelty; -1 means the problem is already solved, preventing resubmit
            else:
                if info[name][3].get(problem, 0) < 0:
                    pass
                else:
                    info[name][0] += 1
                    info[name][1] += time + info[name][3].get(problem, 0)
                    info[name][3][problem] = -1
        elif stat == 'I':
            if name not in info:
                info[name] = [0, 0, name, {problem:20}]
            else:
                if info[name][3].get(problem, 0) < 0:
                    pass
                else:
                    info[name][3][problem] = info[name][3].get(problem, 0) + 20
        else:
            if name not in info:
                info[name] = [0, 0, name, {}]

        input = sys.stdin.readline().strip()
    
    result = sorted(info.values(), key = lambda x: (-x[0], x[1], x[2]))
    for i in range(len(result)):
        print('{:d} {:d} {:d}'.format(result[i][2], result[i][0], result[i][1]))
    if count != N-1:
        print()


