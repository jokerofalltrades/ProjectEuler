sum_var = 0
for i in range(1000):
    sum_var += i if i % 3 == 0 or i % 5 == 0 else 0
print(sum_var)
