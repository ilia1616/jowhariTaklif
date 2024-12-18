# x0 = input().split()

# first_line = []
# for i in x0:
#     first_line.append(i.split(','))
# first_line = sorted(first_line)    

# x1 = input().split()
# second_line = []
# for i in x1:
#     second_line.append(i.split(','))
# second_line = sorted(second_line)
    

# if (float(first_line[1][0]) - float(first_line[0][0])) != 0 and (float(second_line[1][0]) - float(second_line[0][0])) != 0:
#     m0 = (float(first_line[1][1]) - float(first_line[0][1])) / (float(first_line[1][0]) - float(first_line[0][0])) # شیب پاره خط 1
#     m1 = (float(second_line[1][1]) - float(second_line[0][1])) / (float(second_line[1][0]) - float(second_line[0][0])) # شیب پاره خط 2
# else:
#     if second_line[0][0] <= first_line[0][0] <= second_line[1][0] or first_line[0][0] <= second_line[0][0] <= first_line[1][0]:
#         print('yes')
    
# # x = (- m0x0 + y0 + m1x1 - y1) / (m1 -m0)
# # فرمول محاسبه طول نقطه ی برخورد

# if m1 != m0:
#     X = (-m0 * float(first_line[0][0]) + float(first_line[0][1]) + m1 * float(second_line[0][0]) - float(second_line[0][1])) / (m1 - m0)
# else:
#     print('no')
    
# if X <= float(first_line[1][0]) and X >= float(first_line[0][0]) and X <= float(second_line[1][0]) and X >= float(second_line[0][0]):
#     print('yes')
# else:
#     print('no')
x0 = input().split()

first_line = []
for i in x0:
    first_line.append(i.split(','))
first_line = sorted(first_line)

x1 = input().split()
second_line = []
for i in x1:
    second_line.append(i.split(','))
second_line = sorted(second_line)

dx0 = float(first_line[1][0]) - float(first_line[0][0])
dx1 = float(second_line[1][0]) - float(second_line[0][0])

# بررسی پاره‌خط‌های عمودی
if dx0 == 0 and dx1 == 0:
    # هر دو پاره‌خط عمودی هستند
    if float(first_line[0][0]) == float(second_line[0][0]):  # اگر x ها برابر باشند
        # بررسی هم‌پوشانی در محور y
        if (
            max(float(first_line[0][1]), float(first_line[1][1])) >= min(float(second_line[0][1]), float(second_line[1][1]))
            and
            max(float(second_line[0][1]), float(second_line[1][1])) >= min(float(first_line[0][1]), float(first_line[1][1]))
        ):
            print("yes")
        else:
            print("no")
    else:
        print("no")
elif dx0 == 0 or dx1 == 0:
    # فقط یکی از پاره‌خط‌ها عمودی است
    print("no")
else:
    # محاسبه شیب‌ها
    m0 = (float(first_line[1][1]) - float(first_line[0][1])) / dx0
    m1 = (float(second_line[1][1]) - float(second_line[0][1])) / dx1

    # بررسی حالت موازی بودن
    if m0 == m1:
        print("no")
    else:
        # محاسبه X
        X = (-m0 * float(first_line[0][0]) + float(first_line[0][1]) + m1 * float(second_line[0][0]) - float(second_line[0][1])) / (m1 - m0)

        if (
            float(first_line[0][0]) <= X <= float(first_line[1][0]) and
            float(second_line[0][0]) <= X <= float(second_line[1][0])
        ):
            print('yes')
        else:
            print('no')
