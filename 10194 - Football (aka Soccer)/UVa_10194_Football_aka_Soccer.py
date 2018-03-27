import sys

input = sys.stdin.readline().strip()

N = int(input)
space_flag = True

for _ in range(N):
    if space_flag:
        space_flag = False
    else:
        print()
    
    input = sys.stdin.readline().strip()
    contest_name = input

    input = sys.stdin.readline().strip()
    num_team = int(input)
    teams = {}
    for _ in range(num_team):
        input = sys.stdin.readline().strip()
        teams[input] = [0 for _ in range(9)]
        # names
        teams[input][0] = input

    input = sys.stdin.readline().strip()
    num_game = int(input)
    for _ in range(num_game):
        input = sys.stdin.readline().strip()
        tmp = input.split('#')
        t1 = tmp[0]
        t2 = tmp[2]
        scores = tmp[1].split('@')
        s1 = int(scores[0])
        s2 = int(scores[1])
        #scores
        teams[t1][7] += s1
        teams[t1][8] += s2
        teams[t1][6] += s1 - s2
        teams[t2][7] += s2
        teams[t2][8] += s1
        teams[t2][6] += s2 - s1
        
        # points and wins
        if s1 > s2:
            teams[t1][1] += 3
            teams[t1][3] += 1
            teams[t2][5] += 1
        elif s1 == s2:
            teams[t1][1] += 1
            teams[t2][1] += 1
            teams[t1][4] += 1
            teams[t2][4] += 1
        else:
            teams[t2][1] += 3
            teams[t2][3] += 1
            teams[t1][5] += 1
        
        # game plyed
        teams[t1][2] += 1
        teams[t2][2] += 1


    sorted_teams = sorted(teams.values(), key = lambda x: (-x[1], -x[3], -x[6], -x[7], x[2], x[0].lower()))
    # sort by rules reversely, which is wrong
    #sorted_teams = sorted(teams.values(), key = lambda x: x[0]) # name
    #sorted_teams = sorted(sorted_teams, key = lambda x: x[2]) # less game played
    #sorted_teams = sorted(sorted_teams, key = lambda x: x[7])[::-1] # most goals scored
    #sorted_teams = sorted(sorted_teams, key = lambda x: x[6])[::-1] # most goals difference
    #sorted_teams = sorted(sorted_teams, key = lambda x: x[3])[::-1] # most wins
    #sorted_teams = sorted(sorted_teams, key = lambda x: x[1])[::-1] # most points earned
    
    # print results
    print(contest_name)
    for i in range(len(sorted_teams)):
        st = [i+1] + sorted_teams[i]
        print("{0:d}) {1:s} {2:d}p, {3:d}g ({4:d}-{5:d}-{6:d}), {7:d}gd ({8:d}-{9:d})".format(*st))



        
    