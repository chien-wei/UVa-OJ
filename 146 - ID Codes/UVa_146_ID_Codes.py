import sys

input = sys.stdin.readline().strip()

while input != '#':
    no_found = True
    for i in range(len(input)-2, -1, -1):
        if input[i] < input[i+1]:
            first = input[:i]
            tmp = ''.join(sorted(input[i:]))
            j = tmp.index(input[i]) + 1 # next smallest alphabet index, need to consider same alphabet
            while tmp[j] == input[i]:
                j += 1
            second = tmp[:j] + tmp[j+1:]
            print(first + tmp[j] + second)
            no_found = False
            break
    if no_found:
        print('No Successor')

    input = sys.stdin.readline().strip()