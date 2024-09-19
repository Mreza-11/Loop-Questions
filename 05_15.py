# 11.
# یک برنامه بنویس که
# اعداد تصادفی 1-10 تولید کنه و چاپ کنه
# وقتی 7 اومد متوقف بشه
import random

x = -1
while x != 7:
    x = random.randrange(1, 11)
    print(x)

print("etmam")
