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
    
   
m0 = (float(first_line[1][1]) - float(first_line[0][1])) / (float(first_line[1][0]) - float(first_line[0][0])) # شیب پاره خط 1
m1 = (float(second_line[1][1]) - float(second_line[0][1])) / (float(second_line[1][0]) - float(second_line[0][0])) # شیب پاره خط 2

# x = (- m0x0 + y0 + m1x1 - y1) / (m1 -m0)
# فرمول محاسبه طول نقطه ی برخورد

X = (-m0 * float(first_line[0][0]) + float(first_line[0][1]) + m1 * float(second_line[0][0]) - float(second_line[0][1])) / (m1 - m0)

if X <= float(first_line[1][0]) and X >= float(first_line[0][0]) and X <= float(second_line[1][0]) and X >= float(second_line[0][0]):
    print('yes')
else:
    print('no')