sum_var = 0
a=1
b=1
while a < 4000000 and b < 4000000:
    c = a + b
    a = b
    b = c
    if b % 2 == 0:
        sum_var += b
print(sum_var)
