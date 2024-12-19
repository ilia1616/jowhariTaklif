from collections import defaultdict
from itertools import product # با این میتونیم تمام حالت های ممکن برای بازی های باقی مانده رو محاسبه کنیم

n = int(input())
d = input() # ['day/month/year']
input()

def change_date(date):
    date = date.split('/')
    return date[::-1]

raw_data = []

for i in range(n):
    raw_data.append(input().split(','))
 
for i in range(len(raw_data)):
     raw_data[i][0] = change_date(raw_data[i][0])
    
sorted_data = sorted(raw_data)    

given_date = change_date(d)

remaining_matches = []

for i in sorted_data:
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
        
# فرض کنید 3 تا بازی باقیمانده داریم
scenarios = list(product(['H', 'D', 'A'], repeat=len(remaining_matches))) # ['H','H','H'] | ['H','H','D'] | ['H','H','A'] | ....

for possible in scenarios:
    