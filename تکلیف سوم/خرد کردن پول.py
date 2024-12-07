n = int(input())

k1 = n // 100
n = n - k1*100
k2 = n //25
n = n - k2*25
k3 = n // 10
n = n - k3*10
# k4 = n 
print(k1 + k2 + k3 + n)