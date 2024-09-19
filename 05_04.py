# برنامه ای بنویسید که
# تعداد اعداد مثبت یک لیست را پیدا کند

l = [1, 2, -3, -9, -5, 4, 9, 9]

# شمارنده
# counter = counter + 1
# counter += 1

import random


l = []

for i in range(5):
    a = random.randrange(-1000, 1000)
    print("a : ", a)
    l.append(a)

print(l)


counter = 0

for i in l:
    if i > 0:
        counter += 1

print("Counter : ", counter)
