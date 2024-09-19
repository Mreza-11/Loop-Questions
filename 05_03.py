# برنامه ای بنویسید که 2 عدد را بگیرد
# اعداد بین آنها را چاپ کند

a = int(input())
b = int(input())

# 1 , 3 => 2
# 2 , 7 => 3 , 4, 5, 6

# print(2 + 1)
# print(a + 2)
# .
# .
# .
# print(7 - 1)

if a > b:
    a, b = b, a

for i in range(a + 1, b):
    print(i)
