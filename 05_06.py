# 4.
# یک عدد بگیره
# مجموع اعداد 1 تا n
# را چاپ کند

# l = [1, 2, 3, ..., n]

sum = 0
n = int(input())

# majmoo = 1 + 2 + 3
# majmoo = 1 + 2 + 3 + 4
# majmoo = 1 + 2 + 3 + 4 + 5

for i in range(1, n + 1):
    sum += i

print(sum)
