import sys

input = sys.stdin.readline().strip()
c = 1
while input != '':
    heights = []
    height = int(input)
    while height != -1:
        heights.append(height)
        input = sys.stdin.readline().strip()
        height = int(input)
    
    if len(heights) == 0:
        input = sys.stdin.readline().strip()
        continue
    LIS = [1 for _ in range(len(heights))]
    for i in range(1, len(heights)):
        for j in range(i-1, -1, -1):
            if heights[j] >= heights[i]:
                LIS[i] = max(LIS[i], LIS[j] + 1)
    if c > 1:
        print()
    print("Test #" + str(c) + ":")
    print("  maximum possible interceptions: " + str(max(LIS)))
    c += 1
    input = sys.stdin.readline().strip()
