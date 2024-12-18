# تابع برای محاسبه مساحت چندضلعی با استفاده از فرمول گیانی(برای فهمیدن فرمول از چت جی پی تی بپرسید)
def calculate_area(points): # یک لیست از نقاط به فرمت [x,y]
    n = len(points) # تعداد نقاط
    area = 0 # تعریف متغیر مساحت
    for i in range(n):
        j = (i + 1) % n # تعریف جِی به عنوان ایندکس بعد از آی (اگر آی ایندکس آخر بود میشود 0)
        area += int(points[i][0]) * int(points[j][1]) 
        area -= int(points[j][0]) * int(points[i][1])
    return int(abs(area) / 2) # از int استفاده میکنیم تا عدد را به پایین گرد کند

# تابع برای محاسبه ضرب متقاطع(همون ضرب برداری در دو بعدی)
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# تابع برای محاسبه چند ضلعی محیط
def convex_hull(points):
    points = sorted(points)  # مرتب کردن نقاط
    lower = []
    for p in points: # محاسبه نقاط نیمه پایینی شکل 
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0: # اعضای لیست lower و یک نقطه را ضرب خارجی میکند و اگر نامثبت بود عضو اخر را از لیست خارج میکند
            lower.pop()
        lower.append(p)
    
    upper = []
    # محاسبه نقاط بالایی شکل
    for p in reversed(points): # برعکس لیست points (ما لیست را برعکس میکنیم تا جهت نقاط پادساعتگرد باشند. چون جهت در فرمول اهمیت دارد)
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0: 
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1] # کل نقاط شکل را برمیگرداند
    # نقطه اخر هر لیست را بر نمیگرداند چون نقطه اخر نیمه بالا همان نقطه اول نیمه پایینی است

# خواندن ورودی
x = input().split()

# تبدیل ورودی به لیست نقاط
points = [tuple(map(int, i.split(','))) for i in x] # اینجااز مپ استفاده کردیم تا اعداد را که به صورت استرینگ هستند را به عدد تبدیل کنیم

# پیدا کردن چند ضلعی محیطی
hull = convex_hull(points)

# محاسبه مساحت چند ضلعی
area = calculate_area(hull)

# چاپ نتیجه (قسمت صحیح مساحت که به سمت پایین گرد شده است)
print(area)