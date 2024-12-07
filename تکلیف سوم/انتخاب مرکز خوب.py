X = input().split()
Y = input().split()

def center_cost(x,y):
    return abs(y)*(x**2)

def cable_cost(x,y,u,v):
    return ((x-u)**2 + (y-v)**2)**0.5

MinTotalCost = 100000000000
index = 0

for i in range(len(X)):
    center = [int(X[i]) , int(Y[i])]
    cost = center_cost(center[0],center[1])
    for j in range(len(X)):
        cost += cable_cost(center[0],center[1],int(X[j]), int(Y[j]))

    # print(cost)
    if cost < MinTotalCost:
        index = i
        MinTotalCost = cost

print(index)
# print(MinTotalCost)