# برنامه ای بنویسید که
# مجموعُ اعداد یک لیست را پیدا کند

import random


l = []

for i in range(5):
    a = random.randrange(-10, 10)
    print("a : ", a)
    l.append(a)

print(l)


sum = 0

for i in l:
    sum += i

print("sum : ", sum)
