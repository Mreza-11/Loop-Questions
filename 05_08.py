# 6
# عدد n رو بگیره
# این شکل رو بکشه :

# *
# * *
# * * *
# * * * *
# * * * * *
# ....
# * * * * * * * *

# n ta khat dare
# har khat be andazeie shomare khat setare
# # dare


import random

a = random.randrange(1, 10)
print("a : ", a)


for i in range(a + 1):
    print(i * "*")
