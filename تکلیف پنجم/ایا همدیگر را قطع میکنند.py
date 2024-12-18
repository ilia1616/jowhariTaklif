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
        # بررسی هم‌پوشانی: اگر شیب‌ها برابر باشند و نقطه‌ای از یک پاره‌خط روی دیگری بیفتد
        b0 = float(first_line[0][1]) - m0 * float(first_line[0][0])  # عرض از مبدا پاره‌خط اول
        b1 = float(second_line[0][1]) - m1 * float(second_line[0][0])  # عرض از مبدا پاره‌خط دوم
        
        if b0 == b1:  # بررسی اینکه آیا خطوط بر روی یکدیگر قرار دارند
            # بررسی هم‌پوشانی بازه‌های پاره‌خط‌ها
            if (
                max(float(first_line[0][0]), float(first_line[1][0])) >= min(float(second_line[0][0]), float(second_line[1][0]))
                and
                max(float(second_line[0][0]), float(second_line[1][0])) >= min(float(first_line[0][0]), float(first_line[1][0]))
            ):
                print("yes")
            else:
                print("no")
        else:
            print("no")
    else:
        # محاسبه X نقطه برخورد
        X = (-m0 * float(first_line[0][0]) + float(first_line[0][1]) + m1 * float(second_line[0][0]) - float(second_line[0][1])) / (m1 - m0)

        if (
            float(first_line[0][0]) <= X <= float(first_line[1][0]) and
            float(second_line[0][0]) <= X <= float(second_line[1][0])
        ):
            print('yes')
        else:
            print('no')
