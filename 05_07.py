# 5.
# یک عدد بگیره
# n!
# را چاپ کند

# n! = 1 * 2 * 3 * ... * n
# 3! = 1 * 2 * 3
# 2! = 1 * 2
# 0! = 1
# 1! = 1

n = int(input())
p = 1

# majmoo = majmoo * i
# majmoo = majmoo * 2
# majmoo = majmoo * 3
# majmoo = majmoo * 4
# .
# .
# .
# .


# 1 => n

for i in range(1, n + 1):
    # majmoo = majmoo * i
    p = p * i


print(p)
