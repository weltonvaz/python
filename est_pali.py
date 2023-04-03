from sympy import divisor_count
count = 0
for num in range(100000001,999999999,2):
    if str(num) == str(num)[::-1]:
        if divisor_count(num) == 2:
            count +=1
print(count)
