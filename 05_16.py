# 13.
# یک برنامه بنویس که
# یک لیست 10 عضوی با اعداد تصادفی (1 تا 6) بسازه
# و نمودارش کنه

# 1 3 5 2 4 =>

# *
# * * *
# * * * * *
# * *
# * * * *

import random

l = []
for _ in range(10):
    x = random.randrange(1, 7)
    l.append(x)

print(l)

for i in l:
    print(i * "*")
