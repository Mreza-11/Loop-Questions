# برنامه ای بنویسید که 5 عدد را بگیرد
# و آنها را در یک لیست ذخیره کند
# و لیست را چاپ کند


import random


l = []

for i in range(5):
    a = random.randrange(1, 1000)
    print("a : ", a)
    l.append(a)

print(l)
