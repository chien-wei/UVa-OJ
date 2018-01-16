'''
@author Chien-Wei Sun
@email chien-wei@outlook.com
@create date 2018-01-16 11:58:31
@modify date 2018-01-16 11:58:31
'''
import sys

if __name__ == '__main__':
    # sys.stdin = open("input.txt")
    t = int(sys.stdin.readline().strip())
    for j in range(t):
        sys.stdin.readline()

        orders = [int(i) for i in sys.stdin.readline().strip().split(' ')]
        if len(orders) == 0:
            continue
        numbers = {}
        for i, n in enumerate(sys.stdin.readline().strip().split(' ')):
            numbers[orders[i]] = n
        ind = sorted(numbers)
        for i in ind:
            print(numbers[i])
        
        if j != t-1:
            print()