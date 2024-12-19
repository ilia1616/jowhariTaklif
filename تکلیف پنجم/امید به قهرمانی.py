# from collections import defaultdict
# from itertools import product # با این میتونیم تمام حالت های ممکن برای بازی های باقی مانده رو محاسبه کنیم

# n = int(input())
# d = input() # ['day/month/year']
# input()

# def change_date(date):
#     date = date.split('/')
#     return date[::-1]

# raw_data = []

# for i in range(n):
#     raw_data.append(input().split(','))
 
# for i in range(len(raw_data)):
#      raw_data[i][0] = change_date(raw_data[i][0])
    
# sorted_data = sorted(raw_data)    

# given_date = change_date(d)

# remaining_matches = []

# for i in sorted_data:
#     if given_date < i[0]:
#         remaining_matches.append(i)
#         sorted_data.remove(i)
        
# teams_score = defaultdict(int)

# for i in sorted_data:
#     if i[5] == "H":
#         teams_score[i[1]] += 3
#     elif i[5] == 'A':
#         teams_score[i[2]] += 3
#     elif i[5] == 'D':
#         teams_score[i[1]] += 1
#         teams_score[i[2]] += 1
        
# # فرض کنید 3 تا بازی باقیمانده داریم
# scenarios = list(product(['H', 'D', 'A'], repeat=len(remaining_matches))) # ['H','H','H'] | ['H','H','D'] | ['H','H','A'] | ....
# winner_chance = defaultdict(int)

# for possible in scenarios:
#     tmp_score = teams_score.copy()

#     for res in range(len(possible)):
#         if possible[res] == 'H':
#             tmp_score[remaining_matches[res][1]] += 3
#         elif possible[res] == 'A':
#             tmp_score[remaining_matches[res][2]] += 3
#         elif possible[res] == 'D':
#             tmp_score[remaining_matches[res][1]] += 1
#             tmp_score[remaining_matches[res][2]] += 1
        
#         print(tmp_score)
            
#     winner_chance[max(tmp_score,key=tmp_score.get)] += 1

# # print(winner_chance)
# final = sorted(winner_chance,key=winner_chance.get,reverse=True)

# for i in final:
#     print(i,end=",")
from collections import defaultdict
from itertools import product # با این میتونیم تمام حالت های ممکن برای بازی های باقی مانده رو محاسبه کنیم

n = int(input())
d = input() # ['day/month/year']
input()

def change_date(date):
    date = date.split('/')
    return list(map(int, date[::-1]))

raw_data = []

for _ in range(n):
    raw_data.append(input().split(','))
 
for i in range(len(raw_data)):
    raw_data[i][0] = change_date(raw_data[i][0])
    
sorted_data = sorted(raw_data, key=lambda x: x[0])    

given_date = change_date(d)

remaining_matches = []

for i in list(sorted_data):
    if given_date < i[0]:
        remaining_matches.append(i)
        sorted_data.remove(i)
        
teams_score = defaultdict(int)

for i in sorted_data:
    if i[5] == "H":
        teams_score[i[1]] += 3
    elif i[5] == 'A':
        teams_score[i[2]] += 3
    elif i[5] == 'D':
        teams_score[i[1]] += 1
        teams_score[i[2]] += 1
        
scenarios = list(product(['H', 'D', 'A'], repeat=len(remaining_matches))) # ['H','H','H'] | ['H','H','D'] | ['H','H','A'] | ....
winner_chance = defaultdict(int)

for possible in scenarios:
    tmp_score = teams_score.copy()

    for res in range(len(possible)):
        if possible[res] == 'H':
            tmp_score[remaining_matches[res][1]] += 3
        elif possible[res] == 'A':
            tmp_score[remaining_matches[res][2]] += 3
        elif possible[res] == 'D':
            tmp_score[remaining_matches[res][1]] += 1
            tmp_score[remaining_matches[res][2]] += 1
        
    max_score = max(tmp_score.values())
    for team, score in tmp_score.items():
        if score == max_score:
            winner_chance[team] += 1

final = sorted(winner_chance, key=winner_chance.get, reverse=True)

print(','.join(final))