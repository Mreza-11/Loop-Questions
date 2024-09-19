# 7.3
# عدد n رو بگیره
# این شکل رو بکشه :

# *  *  *  *  *  *  *  *
# *                    *
# *                    *
# *                    *
# *                    *
# *                    *
# *                    *
# *  *  *  *  *  *  *  *

import random

n = random.randrange(2, 10)
print("n : ", n, end="\n\n")

print(n * "* ")

for i in range(n - 2):
    print("*", (2 * n - 5) * " ", "* ")

print(n * "* ")
