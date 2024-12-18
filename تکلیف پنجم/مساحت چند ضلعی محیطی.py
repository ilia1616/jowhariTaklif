x = input().split()

points = []
for i in x:
    points.append(i.split(','))

def m(Z):
    return Z[1]

X = sorted(points) # مرتب کردن بر اساس طول
Y = sorted(points, key=m)
# pointsY = sorted(points, key=lambda x: x[1])

