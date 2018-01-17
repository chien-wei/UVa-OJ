'''
@author Chien-Wei Sun
@email chien-wei@outlook.com
@create date 2018-01-16 11:58:31
@modify date 2018-01-16 11:58:31
'''
# i = 1

# s = '{:032b}'.format(1)
# print([s[i:i+8] for i in range(0, len(s), 8)])
# s = '{:032b}'.format(16777216)
# print([s[i:i+8] for i in range(0, len(s), 8)])

# s = '{:032b}'.format(123456789)
# print([s[i:i+8] for i in range(0, len(s), 8)])
# s = '{:032b}'.format(365779719)
# print([s[i:i+8] for i in range(0, len(s), 8)])
# print(s)

# s = '{:032b}'.format(-123456789)
# print([s[i:i+8] for i in range(0, len(s), 8)])
# s = '{:032b}'.format(-349002504)
# print([s[i:i+8] for i in range(0, len(s), 8)])
# print(s)

# s = '{:032b}'.format(20034556)
# print([s[i:i+8] for i in range(0, len(s), 8)])
# s = '{:032b}'.format(-55365375)
# print([s[i:i+8] for i in range(0, len(s), 8)])
# print(s)

# s = '{:032b}'.format(-1)
# print([s[i:i+8] for i in range(0, len(s), 8)])
# s = '{:032b}'.format(-4294967295)
# print([s[i:i+8] for i in range(0, len(s), 8)])
# print(s)


# print(int("11111111111111111111111111111111", 2), 4294967296 - 1)
# print(int("11111111111111111111111111111110", 2), 4294967296 - 2)
# print(int("10000000000000000000000000000000", 2), 4294967296 - 2147483648)

# 10000000 00000000 00000000 00000000 => -2147483648
# 11111111 11111111 11111111 11111111 => -1


import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline().strip()
while input:
    if input[0] == '-':
        # this s is unsigned to signed
        s = '{:032b}'.format(4294967296 - int(input[1:]))
        s = [s[i:i+8] for i in range(0, len(s), 8)][::-1]
        s = ''.join(s)
        if s[0] == '1':
            print(str(input) + ' converts to ' + str( int(s, 2) - 4294967296))
        else:
            print(str(input) + ' converts to ' + str(int(s, 2))) 
        
    else:
        s = '{:032b}'.format(int(input))
        s = [s[i:i+8] for i in range(0, len(s), 8)][::-1]
        s = ''.join(s)
        if s[0] == '1':
            print(str(input) + ' converts to ' + str( int(s, 2) - 4294967296))
        else:
            print(str(input) + ' converts to ' + str(int(s, 2))) 

    input = sys.stdin.readline().strip()

