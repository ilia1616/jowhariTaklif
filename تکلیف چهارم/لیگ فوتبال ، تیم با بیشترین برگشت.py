# گرفتن تعداد بازی ها
n = int(input())
# بعدا به اینا نیاز داریم
data= []
comeBacks = {}

# دریافت اطلاعات بازی ها
for i in range(n):
    if i == 0:
        continue # یعنی اولین خطی که به عنوان ورودی میده رو بیخیال شو (همون سر تیتر هایی که ما لازمشون نداریم) 
    data.append(input().split(',')) # تبدیل رشته ها به لیست
 
for j in data:
    homeTeam = j[1] # تیم میزبان
    awayTeam = j[2] # مهمان
    homeGoal = j[3] # تعداد گل میزبان
    awayGoal = j[4] # تعداد گل مهمان
    comeBacks[homeTeam] = 0 # وارد کردن اسم تیم میزبان به دیکشنری و قرار دادن مقدار ان
    comeBacks[awayTeam] = 0 # وارد کردن اسم تیم مهمان در دیکشنری و قرار دادن مقدار ان

    # تحلیل وضعیت نیمه اول
    '''
    چک کنیم ببینیم توی نیمه اول کدوم تیم جلو تر بوده و بعدا اگه نتیجه نهایی بازی با نیمه اول تفاوت داشت به عنوان کام بک در نظر بگیریم
    '''

    if homeGoal > awayGoal: 
        tmp = 'H'
    elif homeGoal < awayGoal:
        tmp = 'A'
    else:
        tmp ='D'
    
    # مقایسه نتیجه نیمه اول با نتیجه نهایی
    # اگر تفاوت داشت به عنوان کام بک در نظر میگیریم
    if j[5] != tmp and j[5] != 'D':
        if tmp == 'A':
            comeBacks[homeTeam] += 1
        else:
            comeBacks[awayTeam] += 1

print(max(comeBacks, key=comeBacks.get))# از توی دیکشنری، کلید با بیشترین مقدار را (تیم با بیشترین کام بک) برگردانp