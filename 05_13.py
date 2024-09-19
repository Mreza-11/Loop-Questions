# 9.
# input n
# اول هست یا نه؟


#  6 : 1 , 2 , 3 , 6 => نیست
#  7 : 1 , 7 => هست
#  269 : 1 , 269 => هست

import random

n = random.randrange(1, 1000)

counter = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        counter += 1

print("counter ", counter)

if counter == 2:
    print("yes")
else:
    print("no")
