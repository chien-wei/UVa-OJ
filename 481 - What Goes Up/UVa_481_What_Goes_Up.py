# the idea see https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
import sys

def ceilIndex(A, target):
    l, r = 0, len(A)
    while r-l > 1:
        m = (l + r) // 2
        if A[m] >= target:
            r = m
        else:
            l = m
    return r


input = sys.stdin.readline().strip()
nums = []
while input != '':
    nums.append(int(input))
    input = sys.stdin.readline().strip()

justTail = []
trails = []
for num in nums:
    flag = ceilIndex(justTail, num)
    #print(flag)
    if flag == len(justTail): # case 2
        # update justTail
        justTail.append(num)
        # update trails
        if len(trails) < 1:
            trails.append([num])
        else:
            trails.append(trails[-1] + [num])
    elif num < justTail[0] and num < trails[0][0]: # case 1
        # update justTail
        justTail[0] = num
        # update trails
        trails[0] = [num]
    else: # case 3
        # update justTail
        justTail[flag] = num
        # update trails
        trails[flag] = trails[flag-1] + [num]
    #print(justTail)
    #print(trails)
print(len(justTail))
print('-')
for n in trails[-1]:
    print(n)


# O(n^2) LIS will get TLE in this problem
'''
import sys

input = sys.stdin.readline().strip()
nums = []
while input != '':
    nums.append(int(input))

    input = sys.stdin.readline().strip()

LIS = [1 for _ in range(len(nums))]
for i in range(1, len(nums)):
    for j in range(i-1, -1, -1):
        if nums[j] < nums[i]:
            LIS[i] = max(LIS[i], LIS[j] + 1)

longest = max(LIS)
print(longest)
print('-')
track = []
c = longest
for i in range(len(nums)-1, -1, -1):
    if LIS[i] == c and LIS[i] == longest:
        track.append(nums[i])
        c -= 1
    elif LIS[i] == c and nums[i] < track[-1]:
        track.append(nums[i])
        c -= 1
for n in track[::-1]:
    print(n)
'''