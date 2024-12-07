n = int(input())
input()
data= []

for i in range(n):
    data.append(input().split(',')) 


def find_team_with_most_consecutive_wins(matches):
    from collections import defaultdict

    win_streaks = defaultdict(int)
    max_streaks = defaultdict(int)

    matches.sort(key=lambda x: x[0])

    for match in matches:
        date, home_team, away_team, ftr = match[0], match[1], match[2], match[5]

        if ftr == 'H':
            winner = home_team
        elif ftr == 'A':
            winner = away_team
        else:
            continue

        win_streaks[winner] += 1
        max_streaks[winner] = max(max_streaks[winner], win_streaks[winner])

        for team in [home_team, away_team]:
            if team != winner:
                win_streaks[team] = 0

    best_team = max(max_streaks, key=max_streaks.get)
    return best_team


print(find_team_with_most_consecutive_wins(data))
