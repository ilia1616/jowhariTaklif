x = input().split()

points = []
for i in x:
    points.append(i.split(','))

def calculate_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2


def do_i_need_this_lower(x0,y0,x1,y1,x2,y2):
    if x2 != x0:
        m = (y2 - y0) / (x2 - x0)
    else:
        return False
    
    if y1 > m * (x1 - x0) + y0:
        return False
    else:
        return True
def do_i_need_this_upper(x0,y0,x1,y1,x2,y2):
    if x2 != x0:
        m = (y2 - y0) / (x2 - x0)
    else:
        return False
    
    if y1 < m * (x1 - x0) + y0:
        return False
    else:
        return True
    
X = sorted(points) # مرتب کردن بر اساس طول
# pointsY = sorted(points, key=lambda x: x[1])

lowerPart = []
upperPart = []
lowerY = X[0][1]
for i in X:
    if i[1] <= lowerY:
        lowerPart.append(i)
    if i[1] >= lowerY:
        upperPart.append(i)
    
neededLowerPart = [lowerPart[0]]
for i in range(len(lowerPart) - 2):
    if do_i_need_this_lower(int(lowerPart[i][0]),int(lowerPart[i][1]),
                   int(lowerPart[i+1][0]), int(lowerPart[i+1][1]),
                    int(lowerPart[(i+2)][0]),int(lowerPart[(i+2)][1])):
        neededLowerPart.append(lowerPart[i+1])
neededLowerPart.append(lowerPart[-1])



neededUpperPart = [upperPart[0]]
for i in range(len(upperPart) - 2):
    if do_i_need_this_upper(int(upperPart[i][0]),int(upperPart[i][1]),
                   int(upperPart[i+1][0]), int(upperPart[i+1][1]),
                    int(upperPart[(i+2)][0]),int(upperPart[(i+2)][1])):
        neededLowerPart.append(lowerPart[i+1])
neededUpperPart.append(upperPart[-1])

Points = tuple(neededLowerPart + neededUpperPart[::-1]) # نقاط به ترتیب پادساعتگرد هستند(برای محاسبه مساحت نیاز داریم که نقاط به ترتیب باشند)
finalPoints = []
for i in Points:
    if i not in finalPoints:
        finalPoints.append(i)
        
print(calculate_area(finalPoints))