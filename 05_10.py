# 7.2
# عدد n رو بگیره
# این شکل رو بکشه :

# *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *

import random

a = random.randrange(1, 10)
print("a : ", a)


for i in range(a):
    print(a * " * ")
