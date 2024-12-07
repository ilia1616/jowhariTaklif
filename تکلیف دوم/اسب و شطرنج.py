kn1 = input().split()
kn2 = input().split()

if (abs(int(kn1[0]) - int(kn2[0])) == 1) and abs(int(kn1[1]) - int(kn2[1])) == 2:
        print(1)
        # print("first")
elif abs(int(kn1[0]) - int(kn2[0])) == 2 and abs(int(kn1[1]) - int(kn2[1])) == 1:
        print(1)
        # print("second")
else:
    print(0)
