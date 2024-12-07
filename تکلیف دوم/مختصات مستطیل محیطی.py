n = input().split()

p = []
for i in n:
    i = i.split(',')
    p.append(i)


maxX = -999999999999999999999999999999999999999999999999999999
maxY = -999999999999999999999999999999999999999999999999999999
minX = 999999999999999999999999999999999999999999999999999999
minY = 999999999999999999999999999999999999999999999999999999


for i in p:
    if int(i[0]) > maxX:
        maxX = int(i[0])
    if int(i[0]) < minX:
        minX = int(i[0])
    if int(i[1]) > maxY:
        maxY = int(i[1])
    if int(i[1]) < minY:
        minY = int(i[1])


# print(maxY,maxX,minX,minY)
X = maxX - minX
Y = maxY - minY

print(X * Y)