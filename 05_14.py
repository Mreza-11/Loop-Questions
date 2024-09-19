# 10.
# input n
# تام هست یا نه

#  6 : 1 + 2 + 3 = 6 => تام هست
#  4 : 1 + 2  = 3 => تام نیست
# 10 : تام نیست


# 100 , 120 , 40 , 1
# sum = 100 + 120 + 40 + 1
# sum = 0
# print(sum)
# sum = sum + 100
# print(sum)
# sum = sum + 120
# print(sum)
# sum = sum + 40
# print(sum)

import random

n = random.randrange(1, 1000)

sum = 0

for i in range(1, n):
    if n % i == 0:
        print(i)
        sum = sum + i


print("sum ", sum)

if sum == n:
    print("yes")
else:
    print("no")
