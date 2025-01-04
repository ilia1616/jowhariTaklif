n = int(input())

final = [[1]]

for i in range(1, n):
    tmp = []
    for j in range(i + 1):
        if j == 0 or j == i:
            tmp.append(1)
        else:
            tmp.append(final[i-1][j-1] + final[i-1][j])
    final.append(tmp)
    
for row in final:
    for i in row:
        print(i,end=" ")
    print()