from collections import defaultdict

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

remaining_match = []

for i in sorted_data:
    if given_date < i[0]:
        remaining_match.append(i)
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
        
