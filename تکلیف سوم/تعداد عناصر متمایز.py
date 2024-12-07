n = input().split()
x =[]
for i in n:
    if i not in x:
        x.append(i)

z = 0
for i in x:
    z += 1
print(z)
# print("True answer: " + str(len(set(n))))