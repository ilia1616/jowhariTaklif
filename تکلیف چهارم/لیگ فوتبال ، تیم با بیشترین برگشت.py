n = int(input())
data= []
comeBacks = {}

for i in range(n):
    if i == 0:
        continue
    data.append(input().split(',')) 
 
for j in data:
    homeTeam = j[1]
    awayTeam = j[2]
    homeGoal = j[3]
    awayGoal = j[4]
    comeBacks[homeTeam] = 0
    comeBacks[awayTeam] = 0
    if homeGoal > awayGoal:
        tmp = 'H'
    elif homeGoal < awayGoal:
        tmp = 'A'
    else:
        tmp ='D'
    
    if j[5] != tmp and j[5] != 'D':
        if tmp == 'A':
            comeBacks[homeTeam] += 1
        else:
            comeBacks[awayTeam] += 1

print(max(comeBacks))