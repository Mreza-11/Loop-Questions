# 8.
# input n
# مقسوم علیه هاش رو چاپ کن

# #  6 : 1 , 2 , 3 , 6
# #  4 : 1 , 2 , 4
import random

n = random.randrange(1, 1000)
print("n : ", n, end="\n\n")

counter = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        counter += 1

print("counter ", counter)

# # مسابقه
