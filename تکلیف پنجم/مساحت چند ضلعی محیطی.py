import math

# تابع برای محاسبه مساحت چندضلعی با استفاده از فرمول گیانی
def calculate_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += int(points[i][0]) * int(points[j][1])
        area -= int(points[j][0]) * int(points[i][1])
    return int(abs(area) / 2)

# تابع برای محاسبه ضرب متقاطع
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# تابع برای محاسبه هول فاصل
def convex_hull(points):
    points = sorted(points)  # مرتب کردن نقاط
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

# خواندن ورودی
x = input().split()

# تبدیل ورودی به لیست نقاط
points = [tuple(map(int, i.split(','))) for i in x]

# پیدا کردن هول فاصل
hull = convex_hull(points)

# محاسبه مساحت هول فاصل
area = calculate_area(hull)

# چاپ نتیجه (قسمت صحیح مساحت که به سمت پایین گرد شده است)
print(area)