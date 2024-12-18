x = input().split()

points = []
for i in x:
    points.append(i.split(','))

def m(Z):
    return Z[1]

def do_i_need_this(x0,y0,x1,y1,x2,y2):
    if x2 != x0:
        m = (y2 - y0) / (x2 - x0)
    else:
        return False
    
    if y1 > m * (x1 - x0) + y0:
        return False
    else:
        return True
    
X = sorted(points) # مرتب کردن بر اساس طول
Y = sorted(points, key=m)
# pointsY = sorted(points, key=lambda x: x[1])

lowerPart = []
lowerY = X[0][1]
for i in X:
    if i[1] <= lowerY:
        lowerPart.append(i)

neededLowerPart = [lowerPart[0]]
for i in range(len(lowerPart) - 2):
    if do_i_need_this(int(lowerPart[i][0]),int(lowerPart[i][1]),
                   int(lowerPart[i+1][0]), int(lowerPart[i+1][1]),
                    int(lowerPart[(i+2)][0]),int(lowerPart[(i+2)][1])):
        neededLowerPart.append(lowerPart[i+1])

neededLowerPart.append(lowerPart[-1])


