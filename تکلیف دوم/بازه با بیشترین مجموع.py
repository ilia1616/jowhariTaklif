n = input().split()
w =[]
for i in n:
    w.append(int(i))

indexes = [0, 0]
maxSON = -999999999999999999999999999

for i in range(len(w)):
    for j in range(i,len(w)):
        SON = sum(w[i:j+1])
        if SON > maxSON:
            maxSON = SON
            indexes[0] = i
            indexes[1] = j

print(f"{indexes[0]} {indexes[1]} {maxSON}")